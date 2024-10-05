# Unit Testing Report


### GitHub Repository URL: https://github.com/Geoffrey24/Milestone1_Group43

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.

**Five self defined functions are:**
1. Food Search 
2. Nutrition Breakdown
3. Nutrition Range Filter
4. Nutrition Level Filter
5. Additional Feature

## 1. **Test Summary**
The table below lists all the self-defined functions corresponding to the five required features of the application and the test functions designed to validate them.

| **Tested Functions** | **Test Functions**                                                                                                                         |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `search_food_item(query)`         | `test_search_food_item_valid()` <br>  `test_search_food_item_invalid()`                                                                    |
| `get_nutrition_breakdown(food)`   | `test_get_nutrition_breakdown_valid()` <br>  `test_get_nutrition_breakdown_invalid()`                                                      |
| `filter_by_nutrient_range(min, max)` | `test_filter_by_nutrient_range_valid()` <br>  `test_filter_by_nutrient_range_invalid()`                                                    |
| `categorize_nutritional_level(nutrient)` | `test_categorize_nutritional_level_low()` <br>  `test_categorize_nutritional_level_mid()`  <br> `test_categorize_nutritional_level_high()` |
| `additional_feature_function()`         | `test_additional_feature_valid()` <br>  `test_additional_feature_invalid()`                                                                  |

---

## 2. **Test Case Details**

### Test Case 1:
- **Test Function/Module**
  - `test_check_input_valid()`
  - `test_check_input_invalid()`
- **Tested Function/Module**
  - `check_input(input)`
- **Description**
  - the check_input(input) function checks if the input is a valid string or not. It returns a print argument saying "input not valid try again" to let the user know there input was not valid. 
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `check_input(apple)`          | `apple`             |
| `check_input(chicken)`        | `chicken`           |
| `check_input(banana)`         | `banana`            |

- **1) Code for the Test Function**
```python
def test_check_input_valid(input)
    assert search_food-valid("cheese") == "Cheese"
    assert search_food_valid("chicken") == "Chicken"
    
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `check_input(table)`          | `Food Not Found `   |
| `check_input(4594859)`        | `Food Not Found`    |

- **2) Code for the Test Function**
```python
def test_check_input_invalid(input)
    assert search_food_invalid("table") == "Food Not Found"
    assert exc_info.type is ValueError
```



### Test Case 2:
- **Test Function/Module**
  - `test_get_nutrition_breakdown_valid()`
  - `test_get_nutrition_breakdown_invalid()`
- **Tested Function/Module**
  - `test_get_nutrition_breakdown(input)`
- **Description**
  - this test checks if the input is valid and ensures the nutrition breakdown is provided, the input is the users search and the output is the nutrition breakdown or an error "food not food"
- **1) Valid Input and Expected Output**  

| **Valid Input**                        | **Expected Output**                                          |
|----------------------------------------|--------------------------------------------------------------|
| `test_get_nutrition_breakdown(Cheese)` | `{"calories": 50, "carbs": 14, "fat": 0.8}`                  |
| `test_get_nutrition_breakdown(Chicken)`| `{"calories": 150, "carbs": 23, "fat": 0.2}`                 |


- **1) Code for the Test Function**
```python
def test_get_nutrient_breakdown_valid(input):
    assert get_nutrient_breakdown_valid("Cheese") == {"calories": 50, "carbs": 14, "fat": 0.8}
    assert get_nutrient_breakdown_valid("Chicken") == {"calories": 150, "carbs": 23, "fat": 0.2}
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                     | **Expected Output** |
|---------------------------------------|---------------------|
| `test_get_nutrition_breakdown(-$59)`  | `"food not found`   |


- **2) Code for the Test Function**
```python
def test_get_nutrient_breakdown_invalid(food_item):
    assert get_nutrient_breakdown_invalid("Chair") == {"Food not found}
    assert exc_info.type is ValueError
```






### Test Case 3:
- **Test Function/Module**
  - `test_filter_by_nutrient_range_valid()`
  - `test_filter_by_nutrient_range_invalid()`
- **Tested Function/Module**
  - `test_filter_by_nutrient_range(min, max)`
- **Description**
  - The purpose of this test to to check whether the filter by nutrient range function is valid and has appropriate parameters, the input is a min and a max and the output is a valid or in invalid. 
- **1) Valid Input and Expected Output**  

| **Valid Input**                           | **Expected Output** |
|-------------------------------------------|---------------------|
| `test_filter_by_nutrient_range(10, 50)`   | `valid input `      |
| `test_filter_by_nutrient_range(3, 6)`     | `valid input`       |


- **1) Code for the Test Function**
```python
def test_filter_by_nutrient_range_valid():
    assert test_filter_by_nutrient_range(10, 50) == "valid input"
    assert test_filter_by_nutrient_range(1, 7) == "valid input"
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                   | **Expected Output** |
|-------------------------------------|---------------------|
| `test_filter_by_nutrient_range(A,8)`| `invalid input`     |


- **2) Code for the Test Function**
```python
def test_filter_by_nutrient_range_invalid():
    assert test_filter_by_nutrient_range($, 7) == "invalid input"
    assert exc_info.type is ValueError
```






### Test Case 4:
- **Test Function/Module**
  - `test_categorize_by_nutrient_level_valid()`
  - `test_categorize_by_nutrient_level_invalid()`
- **Tested Function/Module**
  - `test_categorize_by_nutrient_level(input)`
- **Description**
  - This function categorize's the input into a small, medium and large sub category based ona  predetermined size and the users input. It requires a search/input to categorize the results as an output. 
- **1) Valid Input and Expected Output**  

| **Valid Input**                            | **Expected Output**                                                |
|--------------------------------------------|--------------------------------------------------------------------|
| `test_categorize_by_nutrient_level(Orange)`| `("valid input", "low") == [{"name": "Orange", "calories": 40}]`   |
| `test_categorize_by_nutrient_level(Cheese)`| `("valid input", "medium") == [{"name": "Cheese", "calories": 50}]`|


- **1) Code for the Test Function**
```python
def categorize_by_nutrient_level_valid():
    assert categorize_by_nutrient_level(food_list, "low") == [{"name": "Orange", "calories": 40}]
    assert categorize_by_nutrient_level(food_list, "medium") == [{"name": "Cheese", "calories": 50}]
    assert categorize_by_nutrient_level(food_list, "high") == [{"name": "Chicken", "calories": 150}]
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_categorize_by_nutrient_level_invalid():
        test_categorize_by_nutrient_level(8594$#) == ("invalid Input")
        assert exc_info.type is ValueError
```







### Test Case 5:
- **Test Function/Module**
  - `test_calculate_total_nutrients_valid()`
  - `test_calculate_total_nutrients_invalid()`
- **Tested Function/Module**
  - `test_calculate_total_nutrients(input)`
- **Description**
  - th purpose of the this test case is to check whether or not the calcute total nutrients functoion has correct parameters and works within the systems capabilites. If not the system will create an error and say "invalid input". The input is the users value while the output is the calculated total nutrients based off the users input. 
- **1) Valid Input and Expected Output**  

| **Valid Input**                                   | **Expected Output**                                   |
|---------------------------------------------------|-------------------------------------------------------|
| `test_calculate_total_nutrients(Cheese, Chicken)` | `total == {"calories": 200, "carbs": 37, "fat": 1}`   |
         


- **1) Code for the Test Function**
```python
def test_calculate_total_nutrients_valid():
  assert test_calculate_total_nutrients(Cheese,Chicken)
  total == {"calories": 200, "carbs": 37, "fat": 1}
    
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                  | **Expected Output** |
|------------------------------------|---------------------|
| `test_calculate_total_nutrients(8)`| `invalid input`     |


- **2) Code for the Test Function**
```python
def test_calculate_total_nutrients_invalid():
    with pytest.raises(ValueError) as exc_info:
        test_calculate_total_nutrients(10, 0) == "invalid input"
    assert exc_info.type is ValueError
```

## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.


testing report summary:

This testing report summarizes the results of unit tests conducted on the functionality of the nutrient calculation features implemented in the application. The tests were designed to validate five key functions: search_food, get_nutrient_breakdown, filter_by_nutrient_range, categorize_by_nutrient_level, and calculate_total_nutrients. Each function was tested for correctness and robustness, ensuring that it handles both valid and edge case inputs effectively.

Testing Methodology
To perform the tests, the following command was executed in the terminal:

command line :
pytest test_all_functions.py --html=unit_test.html --self-contained-html

This command runs all the test functions defined in test_all_functions.py and generates an HTML report (unit_test.html) showcasing the test results.

Key Features Tested:

search_food(food_name): Verified that the function correctly returns food names or error messages.
get_nutrient_breakdown(food_item): Confirmed that it retrieves accurate nutrient data for specified food items.
filter_by_nutrient_range(food_list, min_value, max_value): Tested its ability to filter food items based on calorie content accurately.
categorize_by_nutrient_level(food_list, level): Ensured that food items were correctly categorized based on their calorie levels.
calculate_total_nutrients(food_list): Validated the summation of nutrient values, including handling of missing keys in the input data.
Test Results
The results of the unit tests are presented in the attached screenshot. All functions passed their respective tests, demonstrating that the implementation meets the expected functionality.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./Unit_test.png)
