"""Glue between Django models and the pure packing logic."""
from typing import Iterable, Tuple

from ..models import Box, Order, Product
from .packing import BoxSpec, Item, PackingError, Recommendation, recommend_box


def _items_from_lines(lines: Iterable[Tuple[Product, int]]):
    items = []
    for product, qty in lines:
        if qty < 1:
            raise PackingError(f"Quantity for {product.sku} must be at least 1.")
        for n in range(qty):
            items.append(Item(f"{product.sku}#{n + 1}", product.length, product.width,
                              product.height, product.weight))
    return items


def _active_box_specs():
    return [BoxSpec(b.id, b.name, b.length, b.width, b.height, b.max_weight, b.cost)
            for b in Box.objects.filter(is_active=True)]


def recommend_for_order(order: Order) -> Recommendation:
    lines = [(i.product, i.quantity) for i in order.items.select_related("product")]
    return recommend_box(_items_from_lines(lines), _active_box_specs())


def recommend_for_lines(lines: Iterable[Tuple[Product, int]]) -> Recommendation:
    return recommend_box(_items_from_lines(lines), _active_box_specs())
