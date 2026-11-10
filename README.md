# Box Selection System

A small Django app that recommends the **cheapest shipping box that physically fits** every item in an order. It has a web page for the warehouse team, a JSON API, and Django admin for managing data.

## Run it

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      Mac/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data        # sample products, boxes and order ORD-1001
python manage.py runserver
```

| URL | What it is |
|---|---|
| http://127.0.0.1:8000/ | Web UI: choose items, get a recommendation |
| http://127.0.0.1:8000/api/orders/ORD-1001/recommend-box/ | API for a stored order |
| http://127.0.0.1:8000/admin/ | Admin (run `python manage.py createsuperuser` first) |

Run the tests with `python manage.py test -v 2`.

## How it decides

For every active box:

1. **Fast rejection**: total weight over the box limit, total volume over the box volume, or any single item bigger than the box (dimensions are compared sorted, so rotation is accounted for).
2. **Real fit check**: a greedy 3D packer places items largest-first at "extreme points", trying all 6 orientations and checking bounds and overlap. This catches cases volume alone misses, for example two 6 cm cubes in a 10 × 10 × 10 box (432 < 1000 cm³, but they cannot sit side by side).
3. **Choice**: among boxes that really fit, pick the **cheapest**. Ties go to the smaller volume, then the lower id, so the result is deterministic.

If nothing fits, the response says so (`recommended_box` is `null`) and explains why each box was rejected.

## API

`POST /api/recommend-box/`

```json
{ "items": [ { "sku": "BOOK-01", "quantity": 2 }, { "sku": "MUG-01" } ] }
```

`GET /api/orders/<reference>/recommend-box/` does the same for a stored order.

Response (abridged):

```json
{
  "message": "Cheapest box that fits all items.",
  "recommended_box": { "id": 2, "name": "Medium", "cost": "18.00",
                       "internal_dimensions_cm": ["35.00", "25.00", "15.00"], "max_weight_kg": "8.000" },
  "total_weight_kg": "1.150",
  "total_volume_cm3": "2660.00",
  "evaluations": [ { "box": "Small", "fits": false, "reason": "items could not be arranged inside the box" },
                   { "box": "Medium", "fits": true, "reason": "fits" } ]
}
```

| Status | When |
|---|---|
| 200 | Success. Also returned when no box fits (`recommended_box` is `null`) |
| 400 | Bad JSON, empty or invalid `items`, quantity not a positive integer, order with no items, or more than 100 items |
| 404 | Unknown SKU or order reference |
| 405 | Wrong HTTP method |

## Project layout

```
config/                  Django settings and root URLs
boxes/
  models.py              Product, Box, Order, OrderItem
  services/packing.py    Pure packing logic (no Django imports)
  services/selector.py   Connects models to the packing logic
  views.py, urls.py      API endpoints and the home page
  templates/, static/    Web UI (HTML, CSS, JavaScript)
  management/commands/   seed_data sample loader
  tests/                 test_packing.py (logic), test_api.py (API and page)
```

Units: dimensions in cm, weight in kg. Box dimensions are **internal** dimensions.

## Assumptions and limitations

- Items are rigid cuboids and can be rotated freely (no "this side up").
- No packing material, fragility or stacking rules. The box weight limit covers contents only.
- 3D bin packing is NP-hard, so the packer is a heuristic. **A "fits" answer is always correct** (placements are checked for bounds and overlap). It may occasionally say "does not fit" for a very tight arrangement a perfect solver would find. That is the safe direction for a warehouse.
- An order needing more than one box is reported as "no single box" rather than split into parcels.
- Orders are limited to 100 items, because the packer's cost grows quickly with item count.
- Only boxes marked active are considered.

## Configuration

Defaults suit local development. For anything else, set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0` and `DJANGO_ALLOWED_HOSTS` (comma separated).

## Tests

41 tests: selection rules, rotation, exact fits, weight and volume boundaries, geometry failures, ties, the item cap, API validation and status codes, and the home page. Latest run: `TEST_OUTPUT.md`. CI: `.github/workflows/tests.yml`.
