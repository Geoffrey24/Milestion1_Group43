# all_functions.py
import random
def search_food_item(query):
    # Simulate food search
    food_db = {"apple": {"calories": 95}, "banana": {"calories": 105}}
    return food_db.get(query)

def get_nutrition_breakdown(food):
    # Simulate nutrition breakdown
    if food not in ["apple", "banana"]:
        return None
    return {"calories": 95 if food == "apple" else 105}

def filter_by_nutrient_range(min, max):
    # Simulate filtering
    nutrients = [("apple", 95), ("banana", 105), ("orange", 80)]
    return [food for food, cal in nutrients if min <= cal <= max]

def categorize_nutritional_level(nutrient):
    if nutrient < 10:
        return "Low"
    elif 10 <= nutrient < 20:
        return "Medium"
    else:
        return "High"

def additional_feature_function(input):
    if input == "valid":
        return "Success"
    else:
        return None
