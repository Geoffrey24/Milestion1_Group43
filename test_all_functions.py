# test_all_functions.py

import pytest
from all_functions import search_food, get_nutrient_breakdown, filter_by_nutrient_range, categorize_by_nutrient_level, calculate_total_nutrients

def test_search_food():
    assert search_food("cheese") == "Cheese"
    assert search_food("chicken") == "Chicken"
    assert search_food("invalid") == "Invalid food, try again."

def test_get_nutrient_breakdown():
    assert get_nutrient_breakdown("Cheese") == {"calories": 50, "carbs": 14, "fat": 0.8}
    assert get_nutrient_breakdown("Chicken") == {"calories": 150, "carbs": 23, "fat": 0.2}
    assert get_nutrient_breakdown("invalid") == {}

def test_filter_by_nutrient_range():
    food_list = [{"name": "Cheese", "calories": 50}, {"name": "Chicken", "calories": 150}]
    result = filter_by_nutrient_range(food_list, 50, 100)
    assert result == [{"name": "Cheese", "calories": 50}]

def test_categorize_by_nutrient_level():
    food_list = [
        {"name": "Cheese", "calories": 50},
        {"name": "Chicken", "calories": 150}
    ]
    low_calories = categorize_by_nutrient_level(food_list, "low")
    medium_calories = categorize_by_nutrient_level(food_list, "medium")
    high_calories = categorize_by_nutrient_level(food_list, "high")

    assert low_calories == []  # Cheese is exactly 50, so it's not low
    assert medium_calories == [{"name": "Cheese", "calories": 50}]  # Cheese is categorized as medium
    assert high_calories == [{"name": "Chicken", "calories": 150}]  # Chicken is categorized as high

def test_calculate_total_nutrients():
    food_list = [
        {"calories": 50, "carbs": 14, "fat": 0.8},
        {"calories": 150, "carbs": 23, "fat": 0.2}
    ]
    result = calculate_total_nutrients(food_list)
    assert result == {"calories": 200, "carbs": 37, "fat": 1.0}

    food_list_with_missing = [
        {"calories": 50, "carbs": 14},  # Missing 'fat'
        {"calories": 150, "fat": 0.2}    # Missing 'carbs'
    ]
    result_with_missing = calculate_total_nutrients(food_list_with_missing)
    assert result_with_missing == {"calories": 200, "carbs": 14, "fat": 0.2}

    empty_food_list = []
    result_empty = calculate_total_nutrients(empty_food_list)
    assert result_empty == {"calories": 0, "carbs": 0, "fat": 0}
