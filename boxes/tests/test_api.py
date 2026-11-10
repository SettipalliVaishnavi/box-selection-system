"""API and web page tests (use the test database)."""
from django.test import TestCase
from django.urls import reverse

from boxes.models import Box, Order, OrderItem, Product


class ApiTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Product.objects.create(sku="BOOK", name="Book", length=20, width=13, height=3, weight="0.4")
        Product.objects.create(sku="DB", name="Dumbbell", length=30, width=12, height=12, weight="10")
        Box.objects.create(name="Small", length=25, width=18, height=10, max_weight=2, cost="10")
        Box.objects.create(name="Large", length=50, width=40, height=30, max_weight=20, cost="35")
        Box.objects.create(name="Retired", length=25, width=18, height=10, max_weight=2, cost="1", is_active=False)

    def post(self, payload):
        return self.client.post(reverse("recommend-box"), payload, content_type="application/json")

    def test_small_order_gets_small_box(self):
        res = self.post({"items": [{"sku": "BOOK", "quantity": 2}]})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["recommended_box"]["name"], "Small")

    def test_quantity_defaults_to_one(self):
        res = self.post({"items": [{"sku": "BOOK"}]})
        self.assertEqual(res.json()["total_weight_kg"], "0.400")

    def test_inactive_box_is_ignored(self):
        res = self.post({"items": [{"sku": "BOOK"}]})
        names = [e["box"] for e in res.json()["evaluations"]]
        self.assertNotIn("Retired", names)

    def test_heavy_order_gets_large_box(self):
        res = self.post({"items": [{"sku": "DB"}]})
        self.assertEqual(res.json()["recommended_box"]["name"], "Large")

    def test_no_box_fits_returns_null_box(self):
        res = self.post({"items": [{"sku": "DB", "quantity": 3}]})
        self.assertEqual(res.status_code, 200)
        self.assertIsNone(res.json()["recommended_box"])

    def test_volume_is_formatted(self):
        res = self.post({"items": [{"sku": "BOOK"}]})
        self.assertEqual(res.json()["total_volume_cm3"], "780.00")

    def test_repeated_sku_lines_are_combined(self):
        res = self.post({"items": [{"sku": "BOOK"}, {"sku": "BOOK"}]})
        self.assertEqual(res.json()["total_weight_kg"], "0.800")

    def test_unknown_sku_is_404(self):
        self.assertEqual(self.post({"items": [{"sku": "NOPE"}]}).status_code, 404)

    def test_empty_items_is_400(self):
        self.assertEqual(self.post({"items": []}).status_code, 400)

    def test_missing_items_is_400(self):
        self.assertEqual(self.post({}).status_code, 400)

    def test_bad_quantity_is_400(self):
        for bad in (0, -1, "2", 1.5, True):
            with self.subTest(quantity=bad):
                self.assertEqual(self.post({"items": [{"sku": "BOOK", "quantity": bad}]}).status_code, 400)

    def test_too_many_items_is_400(self):
        res = self.post({"items": [{"sku": "BOOK", "quantity": 101}]})
        self.assertEqual(res.status_code, 400)
        self.assertIn("limit", res.json()["error"])

    def test_invalid_json_is_400(self):
        res = self.client.post(reverse("recommend-box"), "{oops", content_type="application/json")
        self.assertEqual(res.status_code, 400)

    def test_get_not_allowed(self):
        self.assertEqual(self.client.get(reverse("recommend-box")).status_code, 405)

    def test_stored_order(self):
        order = Order.objects.create(reference="ORD-1")
        OrderItem.objects.create(order=order, product=self.book, quantity=1)
        res = self.client.get(reverse("order-recommend-box", args=["ORD-1"]))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["recommended_box"]["name"], "Small")

    def test_stored_order_not_found(self):
        self.assertEqual(self.client.get(reverse("order-recommend-box", args=["X"])).status_code, 404)

    def test_stored_order_without_items_is_400(self):
        Order.objects.create(reference="EMPTY")
        self.assertEqual(self.client.get(reverse("order-recommend-box", args=["EMPTY"])).status_code, 400)


class HomePageTests(TestCase):
    def test_lists_products_and_only_active_boxes(self):
        Product.objects.create(sku="BOOK", name="Paperback", length=20, width=13, height=3, weight="0.4")
        Box.objects.create(name="Small", length=25, width=18, height=10, max_weight=2, cost="10")
        Box.objects.create(name="Retired", length=25, width=18, height=10, max_weight=2, cost="1", is_active=False)
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Paperback")
        self.assertContains(res, "Small")
        self.assertNotContains(res, "Retired")

    def test_empty_state(self):
        res = self.client.get("/")
        self.assertContains(res, "No products yet")
        self.assertContains(res, "No active boxes")

    def test_static_assets_are_linked(self):
        res = self.client.get("/")
        self.assertContains(res, "boxes/style.css")
        self.assertContains(res, "boxes/app.js")
