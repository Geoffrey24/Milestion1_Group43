# all_functions.py

def search_food(food_name):
    food_db = {"cheese": "Cheese", "chicken": "Chicken"}
    return food_db.get(food_name.lower(), "Invalid food, try again.")

def get_nutrient_breakdown(food_item):
    nutrient_data = {
        "Cheese": {"calories": 50, "carbs": 14, "fat": 0.8},
        "Chicken": {"calories": 150, "carbs": 23, "fat": 0.2},
    }
    return nutrient_data.get(food_item, {})

def filter_by_nutrient_range(food_list, min_value, max_value):
    return [food for food in food_list if min_value <= food['calories'] <= max_value]

def categorize_by_nutrient_level(food_list, level):
    categories = {
        "low": lambda x: x['calories'] < 50,
        "medium": lambda x: 50 <= x['calories'] < 100,
        "high": lambda x: x['calories'] >= 100,
    }
    return [{"name": food['name'], "calories": food['calories']} for food in food_list if categories[level](food)]

def calculate_total_nutrients(food_list):
    total_nutrients = {"calories": 0, "carbs": 0, "fat": 0}
    for food in food_list:
        for nutrient in total_nutrients:
            total_nutrients[nutrient] += food.get(nutrient, 0)
    return total_nutrients