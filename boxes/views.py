
import json
from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Box, Order, Product
from .services.packing import PackingError, Recommendation
from .services.selector import recommend_for_lines, recommend_for_order


def _volume(value: Decimal) -> str:
    return str(value.quantize(Decimal("0.01")))


def _serialize(rec: Recommendation) -> dict:
    return {
        "message": rec.message,
        "recommended_box": (
            None
            if rec.box is None
            else {
                "id": rec.box.id,
                "name": rec.box.name,
                "cost": str(rec.box.cost),
                "internal_dimensions_cm": [
                    str(rec.box.length),
                    str(rec.box.width),
                    str(rec.box.height),
                ],
                "max_weight_kg": str(rec.box.max_weight),
            }
        ),
        "total_weight_kg": str(rec.total_weight),
        "total_volume_cm3": _volume(rec.total_volume),
        "evaluations": [
            {
                "box": evaluation.box.name,
                "fits": evaluation.fits,
                "reason": evaluation.reason,
            }
            for evaluation in rec.evaluations
        ],
    }


def _error(message, status=400):
    return JsonResponse({"error": message}, status=status)


@csrf_exempt
@require_http_methods(["POST"])
def recommend_from_payload(request):
    """POST {"items": [{"sku": "ABC", "quantity": 2}]}"""

    try:
        data = json.loads(request.body or b"{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return _error("Invalid JSON body.")

    raw = data.get("items") if isinstance(data, dict) else None

    if not isinstance(raw, list) or not raw:
        return _error("'items' must be a non-empty list.")

    lines = []

    for entry in raw:
        if not isinstance(entry, dict) or "sku" not in entry:
            return _error("Each item needs a 'sku'.")

        quantity = entry.get("quantity", 1)

        if (
            isinstance(quantity, bool)
            or not isinstance(quantity, int)
            or quantity < 1
        ):
            return _error("'quantity' must be a positive integer.")

        try:
            product = Product.objects.get(sku=entry["sku"])
        except Product.DoesNotExist:
            return _error(f"Unknown SKU: {entry['sku']}", 404)

        lines.append((product, quantity))

    try:
        recommendation = recommend_for_lines(lines)
        return JsonResponse(_serialize(recommendation))
    except PackingError as exc:
        return _error(str(exc))


@require_http_methods(["GET"])
def recommend_for_existing_order(request, reference):
    try:
        order = Order.objects.get(reference=reference)
    except Order.DoesNotExist:
        return _error(f"Order not found: {reference}", 404)

    try:
        recommendation = recommend_for_order(order)
        return JsonResponse(_serialize(recommendation))
    except PackingError as exc:
        return _error(str(exc))


@require_http_methods(["GET"])
def index(request):
    """Display products and available boxes."""

    products = Product.objects.order_by("name")
    boxes = Box.objects.filter(is_active=True).order_by("cost")

    return render(
        request,
        "boxes/index.html",
        {
            "products": products,
            "boxes": boxes,
        },
    )
