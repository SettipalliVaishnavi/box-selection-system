# Box Selection System

A Django-based Box Selection System that recommends the **cheapest shipping box capable of physically fitting all items in an order**.

The application provides a warehouse-friendly web interface, REST API endpoints for box recommendations, and Django Admin for managing products, shipping boxes, and orders.

## Features

- Recommends the cheapest box that can accommodate all items in an order.
- Supports 3D item rotation to maximize packing efficiency.
- Checks box weight limits and internal dimensions.
- Uses a 3D packing algorithm to verify whether items physically fit.
- Provides a web-based interface for warehouse operations.
- Exposes JSON API endpoints for integration with other applications.
- Includes Django Admin for managing products, boxes, and orders.
- Provides detailed rejection reasons when a box cannot accommodate an order.
- Includes automated tests covering packing logic, API validation, and application functionality.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd box_selector_project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Load sample data

```bash
python manage.py seed_data
```

This command creates sample products, shipping boxes, and an example order (`ORD-1001`).

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

| URL | Description |
|---|---|
| http://127.0.0.1:8000/ | Main application interface |
| http://127.0.0.1:8000/api/orders/ORD-1001/recommend-box/ | Order-based box recommendation API |
| http://127.0.0.1:8000/admin/ | Django Admin dashboard |

To access Django Admin, first create a superuser:

```bash
python manage.py createsuperuser
```

## Box Selection Algorithm

The application follows a three-stage process to identify the most suitable shipping box.

### 1. Initial Validation and Rejection

Each active box is checked against the following conditions:

- Total item weight must not exceed the box's maximum weight capacity.
- Total item volume must not exceed the box's internal volume.
- Each individual item must fit within the box dimensions.
- Item dimensions are sorted before comparison to account for rotation.

### 2. 3D Packing Verification

A greedy 3D packing algorithm verifies whether all items can physically fit inside a box.

The algorithm:

- Sorts items from largest to smallest.
- Evaluates six possible orientations for each item.
- Uses extreme points to identify possible item placements.
- Checks box boundaries and overlapping placements.
- Rejects arrangements that cannot accommodate all items.

This approach handles cases where total volume alone cannot guarantee a valid physical arrangement.

### 3. Cheapest Box Selection

After evaluating all active boxes:

- Only boxes that successfully pass the physical packing check are considered.
- The box with the lowest shipping cost is selected.
- If multiple boxes have the same cost, the smaller-volume box is preferred.
- If a tie still exists, the box with the lower database ID is selected.

If no available box can accommodate the order, the API returns a response indicating that no suitable single box was found.

## API Documentation

### 1. Recommend a Box for Items

**Endpoint:**

```http
POST /api/recommend-box/
```

**Sample Request:**

```json
{
  "items": [
    {
      "sku": "BOOK-01",
      "quantity": 2
    },
    {
      "sku": "MUG-01"
    }
  ]
}
```

**Sample Response:**

```json
{
  "message": "Cheapest box that fits all items.",
  "recommended_box": {
    "id": 2,
    "name": "Medium",
    "cost": "18.00",
    "internal_dimensions_cm": [
      "35.00",
      "25.00",
      "15.00"
    ],
    "max_weight_kg": "8.000"
  },
  "total_weight_kg": "1.150",
  "total_volume_cm3": "2660.00",
  "evaluations": [
    {
      "box": "Small",
      "fits": false,
      "reason": "items could not be arranged inside the box"
    },
    {
      "box": "Medium",
      "fits": true,
      "reason": "fits"
    }
  ]
}
```

### 2. Recommend a Box for an Existing Order

**Endpoint:**

```http
GET /api/orders/<reference>/recommend-box/
```

Example:

```http
GET /api/orders/ORD-1001/recommend-box/
```

This endpoint retrieves an existing order and evaluates the available boxes to recommend the cheapest suitable option.

### API Status Codes

| Status Code | Description |
|---|---|
| 200 | Successful recommendation or no suitable box found |
| 400 | Invalid JSON, missing items, invalid quantity, empty order, or item limit exceeded |
| 404 | Unknown product SKU or order reference |
| 405 | Unsupported HTTP method |

## Project Structure

```text
box_selector_project/
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── boxes/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   │
│   ├── services/
│   │   ├── packing.py
│   │   └── selector.py
│   │
│   ├── templates/
│   ├── static/
│   │
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py
│   │
│   └── tests/
│       ├── test_packing.py
│       └── test_api.py
│
├── requirements.txt
├── manage.py
└── README.md
```

## Technical Details

| Component | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| API | JSON-based REST endpoints |
| Testing | Django Test Framework |
| Version Control | Git and GitHub |

**Measurement Units:**
- Dimensions: Centimeters (cm)
- Weight: Kilograms (kg)
- Volume: Cubic centimeters (cm³)
- Box cost: Currency units as configured in the sample data.

## Assumptions and Limitations

- Items are treated as rigid 3D cuboids.
- Items can be rotated freely in all six orientations.
- Fragility, stacking restrictions, and additional packing materials are not considered.
- Box weight capacity applies only to the items inside the box.
- The packing algorithm uses a heuristic approach because 3D bin packing is an NP-hard problem.
- Every successful fit is verified using placement boundaries and overlap checks.
- The heuristic may occasionally reject a valid arrangement, but it does not report an invalid physical placement as a successful fit.
- Orders requiring multiple boxes are reported as having no suitable single box.
- Each order is limited to a maximum of 100 items.
- Only active shipping boxes are considered.

## Configuration

The application uses default settings for local development.

For production environments, configure the following environment variables:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=your-domain.com
```

Do not commit sensitive environment variables or secret keys to GitHub.

## Testing

The project includes **41 automated test cases** covering:

- Box selection rules.
- Item rotation and orientation.
- Exact dimension fits.
- Weight and volume boundaries.
- Physical packing and collision detection.
- Cheapest-box selection.
- Tie-breaking conditions.
- Maximum item limits.
- API request validation.
- HTTP status codes.
- Home page functionality.

Run the test suite using:

```bash
python manage.py test -v 2
```

**Latest Test Results:** 41 tests passed successfully.

Refer to `TEST_OUTPUT.md` for the latest test execution details.

## Continuous Integration

The project includes a GitHub Actions workflow:

```text
.github/workflows/tests.yml
```

This workflow runs automated tests to help verify application functionality during development and code changes.

## Future Enhancements

- Support multiple-box recommendations for large orders.
- Introduce advanced 3D packing optimization algorithms.
- Include packaging material and shipping constraints.
- Add visual 3D representations of box arrangements.
- Improve packing efficiency for complex orders.

## Conclusion

The Box Selection System simplifies shipping box selection by combining weight validation, volume checks, and 3D physical packing verification.

It helps warehouse teams identify the **most cost-effective box that can safely accommodate an entire order**, reducing unnecessary packaging costs and improving shipping efficiency.
