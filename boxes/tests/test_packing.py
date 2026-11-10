"""Unit tests for the pure packing logic (no database needed)."""
from decimal import Decimal as D

from django.test import SimpleTestCase

from boxes.services.packing import (
    MAX_ITEMS_PER_ORDER, BoxSpec, Item, PackingError, can_pack, recommend_box,
)


def item(l, w, h, wt="1", label="i"):
    return Item(label, D(str(l)), D(str(w)), D(str(h)), D(str(wt)))


def box(id, l, w, h, mw, cost):
    return BoxSpec(id, f"B{id}", D(str(l)), D(str(w)), D(str(h)), D(str(mw)), D(str(cost)))


class SelectionTests(SimpleTestCase):
    def test_single_item_picks_the_box_that_fits(self):
        rec = recommend_box([item(5, 5, 5)], [box(1, 3, 3, 3, 5, 1), box(2, 10, 10, 10, 5, 5)])
        self.assertEqual(rec.box.id, 2)

    def test_cheapest_wins_even_if_bigger(self):
        rec = recommend_box([item(5, 5, 5)], [box(1, 10, 10, 10, 5, 9), box(2, 20, 20, 20, 5, 4)])
        self.assertEqual(rec.box.id, 2)

    def test_tie_on_cost_prefers_smaller_volume(self):
        rec = recommend_box([item(5, 5, 5)], [box(1, 20, 20, 20, 5, 5), box(2, 10, 10, 10, 5, 5)])
        self.assertEqual(rec.box.id, 2)

    def test_full_tie_is_deterministic_by_id(self):
        boxes = [box(2, 10, 10, 10, 5, 5), box(1, 10, 10, 10, 5, 5)]
        self.assertEqual(recommend_box([item(5, 5, 5)], boxes).box.id, 1)

    def test_totals_reported(self):
        rec = recommend_box([item(2, 2, 2, "1.5"), item(1, 1, 1, "0.5")], [box(1, 10, 10, 10, 5, 5)])
        self.assertEqual(rec.total_weight, D("2.0"))
        self.assertEqual(rec.total_volume, D("9"))


class FitRuleTests(SimpleTestCase):
    def test_rotation_allows_fit(self):
        rec = recommend_box([item(5, 5, 30)], [box(1, 30, 6, 6, 5, 5)])
        self.assertIsNotNone(rec.box)

    def test_exact_fit(self):
        rec = recommend_box([item(10, 20, 30)], [box(1, 30, 20, 10, 5, 5)])
        self.assertIsNotNone(rec.box)

    def test_item_too_large_rejected(self):
        rec = recommend_box([item(40, 5, 5)], [box(1, 30, 30, 30, 50, 5)])
        self.assertIsNone(rec.box)
        self.assertIn("too large", rec.evaluations[0].reason)

    def test_weight_over_limit_rejected(self):
        rec = recommend_box([item(5, 5, 5, "6")], [box(1, 30, 30, 30, 5, 5)])
        self.assertIsNone(rec.box)
        self.assertIn("weight", rec.evaluations[0].reason)

    def test_weight_exactly_at_limit_is_ok(self):
        rec = recommend_box([item(5, 5, 5, "5")], [box(1, 30, 30, 30, 5, 5)])
        self.assertIsNotNone(rec.box)

    def test_combined_weight_is_checked(self):
        items = [item(1, 1, 1, "3", "a"), item(1, 1, 1, "3", "b")]
        rec = recommend_box(items, [box(1, 30, 30, 30, 5, 5)])
        self.assertIsNone(rec.box)

    def test_total_volume_over_limit_rejected(self):
        items = [item(10, 10, 10, label="a"), item(10, 10, 10, label="b")]
        rec = recommend_box(items, [box(1, 10, 10, 15, 50, 5)])
        self.assertIsNone(rec.box)
        self.assertIn("volume", rec.evaluations[0].reason)

    def test_volume_ok_but_geometry_fails(self):
        # Each 6 cm cube fits alone and 2 x 216 = 432 < 1000 cm3, but two 6 cm cubes
        # cannot sit side by side inside 10 cm in any direction.
        items = [item(6, 6, 6, label="a"), item(6, 6, 6, label="b")]
        rec = recommend_box(items, [box(1, 10, 10, 10, 50, 5)])
        self.assertIsNone(rec.box)
        self.assertIn("arranged", rec.evaluations[0].reason)

    def test_eight_cubes_fill_a_box_perfectly(self):
        items = [item(10, 10, 10, label=str(n)) for n in range(8)]
        self.assertTrue(can_pack(items, box(1, 20, 20, 20, 50, 5)))

    def test_nine_cubes_do_not_fit_the_same_box(self):
        items = [item(10, 10, 10, label=str(n)) for n in range(9)]
        self.assertFalse(can_pack(items, box(1, 20, 20, 20, 50, 5)))


class EdgeCaseTests(SimpleTestCase):
    def test_no_boxes_available(self):
        rec = recommend_box([item(1, 1, 1)], [])
        self.assertIsNone(rec.box)
        self.assertIn("No boxes", rec.message)

    def test_no_box_fits_explains_split(self):
        rec = recommend_box([item(100, 100, 100)], [box(1, 10, 10, 10, 5, 5)])
        self.assertIsNone(rec.box)
        self.assertIn("multiple parcels", rec.message)

    def test_empty_order_raises(self):
        with self.assertRaises(PackingError):
            recommend_box([], [box(1, 10, 10, 10, 5, 5)])

    def test_non_positive_item_raises(self):
        with self.assertRaises(PackingError):
            recommend_box([item(0, 1, 1)], [box(1, 10, 10, 10, 5, 5)])

    def test_too_many_items_raises(self):
        items = [item(1, 1, 1, label=str(n)) for n in range(MAX_ITEMS_PER_ORDER + 1)]
        with self.assertRaises(PackingError):
            recommend_box(items, [box(1, 100, 100, 100, 500, 5)])

    def test_max_items_still_allowed(self):
        items = [item(1, 1, 1, label=str(n)) for n in range(MAX_ITEMS_PER_ORDER)]
        rec = recommend_box(items, [box(1, 100, 100, 100, 500, 5)])
        self.assertIsNotNone(rec.box)
