# test_all_functions.py

import pytest
from all_functions import (search_food_item, get_nutrition_breakdown, filter_by_nutrient_range, categorize_nutritional_level, additional_feature_function)

def test_search_food_item_valid():
    assert search_food_item("apple") == {"calories": 95}

def test_search_food_item_invalid():
    assert search_food_item("non_existent_food") is None

def test_get_nutrition_breakdown_valid():
    assert get_nutrition_breakdown("apple") == {"calories": 95}

def test_get_nutrition_breakdown_invalid():
    assert get_nutrition_breakdown("non_existent_food") is None

def test_filter_by_nutrient_range_valid():
    assert filter_by_nutrient_range(90, 100) == ["apple"]

def test_filter_by_nutrient_range_invalid():
    assert filter_by_nutrient_range(200, 300) == []

def test_categorize_nutritional_level_low():
    assert categorize_nutritional_level(5) == "Low"

def test_categorize_nutritional_level_mid():
    assert categorize_nutritional_level(15) == "Medium"

def test_categorize_nutritional_level_high():
    assert categorize_nutritional_level(30) == "High"

def test_additional_feature_valid():
    assert additional_feature_function("valid") == "Success"

def test_additional_feature_invalid():
    assert additional_feature_function("invalid") is None
