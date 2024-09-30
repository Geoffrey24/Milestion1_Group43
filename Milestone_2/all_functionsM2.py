# all_functions
#This file tests the functions by using hard coded functions


def search_food(food_name):
    food_db = {"Cheese": "cheese", "chicken": "Chicken"}
    return food_db.get(food_name.lower(), "Invalid Food try again ")

def get_nutrient_breakdown(food_item):
    nutrient_data = {
        "Cheese": {"calories": 50, "carbs": 14, "fat": 0.8}, #Example data
        "Chicken": {"calories": 150, "carbs": 23, "fat": 0.2},
    }
    return nutrient_data.get(food_item, {})

def filter_by_nutrient_range(food_list, min_value, max_value):
    return [food for food in food_list if min_value <= food['calories'] <= max_value]

def categorize_by_nutrient_level(food_list, level):
    # Categorize based on calories for simplicity
    categories = {
        "low": lambda x: x['calories'] < 50, #if calories are less than 50 they are catorgoriz{"name": "Cheese", "calories": 50}ed as low,
        "medium": lambda x: 50 <= x['calories'] < 100, #if calories are less than 100 but greater than 50 they are catorgorized as medium,
        "high": lambda x: x['calories'] >= 100, #if calories are greater than or equal to 100 they are catorgorized as high,
    }
    return [food for food in food_list if categories[level](food)]

def calculate_total_nutrients(food_list):
    total_nutrients = {"calories": 0, "carbs": 0, "fat": 0}
    for food in food_list:
        for nutrient in total_nutrients:
            total_nutrients[nutrient] += food.get(nutrient, 0)
    return total_nutrients
