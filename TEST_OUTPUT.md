# Test Output

Command: `python manage.py test -v 2` (Python 3.12.10, Windows, Django 6.1.3)

```
Found 41 test(s).
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, boxes, contenttypes, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying boxes.0001_initial... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_bad_quantity_is_400 (boxes.tests.test_api.ApiTests.test_bad_quantity_is_400) ... ok
test_empty_items_is_400 (boxes.tests.test_api.ApiTests.test_empty_items_is_400) ... ok
test_get_not_allowed (boxes.tests.test_api.ApiTests.test_get_not_allowed) ... ok
test_heavy_order_gets_large_box (boxes.tests.test_api.ApiTests.test_heavy_order_gets_large_box) ... ok
test_inactive_box_is_ignored (boxes.tests.test_api.ApiTests.test_inactive_box_is_ignored) ... ok
test_invalid_json_is_400 (boxes.tests.test_api.ApiTests.test_invalid_json_is_400) ... ok
test_missing_items_is_400 (boxes.tests.test_api.ApiTests.test_missing_items_is_400) ... ok
test_no_box_fits_returns_null_box (boxes.tests.test_api.ApiTests.test_no_box_fits_returns_null_box) ... ok
test_quantity_defaults_to_one (boxes.tests.test_api.ApiTests.test_quantity_defaults_to_one) ... ok
test_repeated_sku_lines_are_combined (boxes.tests.test_api.ApiTests.test_repeated_sku_lines_are_combined) ... ok
test_small_order_gets_small_box (boxes.tests.test_api.ApiTests.test_small_order_gets_small_box) ... ok
test_stored_order (boxes.tests.test_api.ApiTests.test_stored_order) ... ok
test_stored_order_not_found (boxes.tests.test_api.ApiTests.test_stored_order_not_found) ... ok
test_stored_order_without_items_is_400 (boxes.tests.test_api.ApiTests.test_stored_order_without_items_is_400) ... ok
test_too_many_items_is_400 (boxes.tests.test_api.ApiTests.test_too_many_items_is_400) ... ok
test_unknown_sku_is_404 (boxes.tests.test_api.ApiTests.test_unknown_sku_is_404) ... ok
test_volume_is_formatted (boxes.tests.test_api.ApiTests.test_volume_is_formatted) ... ok
test_empty_state (boxes.tests.test_api.HomePageTests.test_empty_state) ... ok
test_lists_products_and_only_active_boxes (boxes.tests.test_api.HomePageTests.test_lists_products_and_only_active_boxes) ... ok
test_static_assets_are_linked (boxes.tests.test_api.HomePageTests.test_static_assets_are_linked) ... ok
test_empty_order_raises (boxes.tests.test_packing.EdgeCaseTests.test_empty_order_raises) ... ok
test_max_items_still_allowed (boxes.tests.test_packing.EdgeCaseTests.test_max_items_still_allowed) ... ok
test_no_box_fits_explains_split (boxes.tests.test_packing.EdgeCaseTests.test_no_box_fits_explains_split) ... ok
test_no_boxes_available (boxes.tests.test_packing.EdgeCaseTests.test_no_boxes_available) ... ok
test_non_positive_item_raises (boxes.tests.test_packing.EdgeCaseTests.test_non_positive_item_raises) ... ok
test_too_many_items_raises (boxes.tests.test_packing.EdgeCaseTests.test_too_many_items_raises) ... ok
test_combined_weight_is_checked (boxes.tests.test_packing.FitRuleTests.test_combined_weight_is_checked) ... ok
test_eight_cubes_fill_a_box_perfectly (boxes.tests.test_packing.FitRuleTests.test_eight_cubes_fill_a_box_perfectly) ... ok
test_exact_fit (boxes.tests.test_packing.FitRuleTests.test_exact_fit) ... ok
test_item_too_large_rejected (boxes.tests.test_packing.FitRuleTests.test_item_too_large_rejected) ... ok
test_nine_cubes_do_not_fit_the_same_box (boxes.tests.test_packing.FitRuleTests.test_nine_cubes_do_not_fit_the_same_box) ... ok
test_rotation_allows_fit (boxes.tests.test_packing.FitRuleTests.test_rotation_allows_fit) ... ok
test_total_volume_over_limit_rejected (boxes.tests.test_packing.FitRuleTests.test_total_volume_over_limit_rejected) ... ok
test_volume_ok_but_geometry_fails (boxes.tests.test_packing.FitRuleTests.test_volume_ok_but_geometry_fails) ... ok
test_weight_exactly_at_limit_is_ok (boxes.tests.test_packing.FitRuleTests.test_weight_exactly_at_limit_is_ok) ... ok
test_weight_over_limit_rejected (boxes.tests.test_packing.FitRuleTests.test_weight_over_limit_rejected) ... ok
test_cheapest_wins_even_if_bigger (boxes.tests.test_packing.SelectionTests.test_cheapest_wins_even_if_bigger) ... ok
test_full_tie_is_deterministic_by_id (boxes.tests.test_packing.SelectionTests.test_full_tie_is_deterministic_by_id) ... ok
test_single_item_picks_the_box_that_fits (boxes.tests.test_packing.SelectionTests.test_single_item_picks_the_box_that_fits) ... ok
test_tie_on_cost_prefers_smaller_volume (boxes.tests.test_packing.SelectionTests.test_tie_on_cost_prefers_smaller_volume) ... ok
test_totals_reported (boxes.tests.test_packing.SelectionTests.test_totals_reported) ... ok

----------------------------------------------------------------------
Ran 41 tests in 0.122s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
```