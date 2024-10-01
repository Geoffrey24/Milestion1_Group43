# Executive Summary

Please provide your GitHub repository link.
### GitHub Repository URL:  https://github.com/Geoffrey24/Milestone1_Group43.git

---


## 1. Food Search
### Description  
 This feature allows users to search for food items in the database and retrieve detailed nutritional information. It acts as the primary interface for users to find specific foods and access data such as calories, fats, proteins, carbohydrates, and vitamins.
### Steps
1. Navigate to the Food 
2. Search tab in the application. 
3. Enter the name of the food item you wish to search for. 
4. Click on the Search button. 
5. View the displayed nutritional information for the selected food item

### Screenshots
Include screenshots for each step demonstrating the use of this feature.  
![1](./visual_design.png)

![2](./visual_design.png)

---

## 2. Nutrition Breakdown
### Description  
The Nutrition Breakdown feature visualizes the distribution of nutrients for any selected food item. Users can view the proportions of different nutrients such as fats, proteins, and carbohydrates in graphical formats like pie charts and bar graphs.
### Steps
1. After performing a food search, select a food item from the results. 
2. Click on the "Nutrition Breakdown" option. 
3. View the pie chart and bar graph displaying the proportion of each nutrient. 
4. Hover over or click specific sections to get additional details on each nutrient.

### Screenshots
Include screenshots for each step demonstrating the use of this feature.  
![1](./visual_design.png)

![2](./visual_design.png)

---

## 3. Filter by nutrition breakdown
### Description  
This function allows the user to filter their search results with a minimum and maxium in categories such as calories and carbohydrates to receive a more customised result. This function will be usable next to the search button for user useability.

### Steps
1. Click "Filter" 
2. Select which nutrient you would like to filter by
3. Set a minimum and maximum
4. Click search


### Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![1](./visual_design.png)

![2](./visual_design.png)


---

## 4. Categorize by nutrient level 
### Description  
By using a predefined threshold for low, medium and high will allow the user to search for a food and recieve an output of the foods nutrients categorized into these pre defined thresholds. It will clearly show the user which foods are high in certain nutrients and which are low. 

### Steps
1. Select the "Categorize" button located near the search button
2. Search for a food
3. CLick on the food
4. A table will be produced with the low, meduim and high contents of that food 

### Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![1](./visual_design.png)

![2](./visual_design.png)


---

## 5. [Feature 5 Name]
### Description  
Briefly describe what this feature does.

descriptions:
fromThe Calculate Total Nutrients feature aggregates the nutrient values (calories, carbs, and fat a list of food items. Each food item is represented 
as a dictionary containing its nutrient information. This feature is useful for users who want to quickly assess their total intake of specific nutrients based on the foods they consume.



### Steps
1. Step-by-step instructions for using this feature.
2. Add additional steps as needed.





Steps
Prepare the Food List:

Create a list of food items, where each item is represented as a dictionary containing nutrient information (e.g., {"calories": 100, "carbs": 20, "fat": 5}).
Invoke the Function:

Call the calculate_total_nutrients(food_list) function, passing the prepared list of food items as the argument.
Review the Output:

The function will return a dictionary summarizing the total nutrient values across all food items, structured as {"calories": total_calories, "carbs": total_carbs, "fat": total_fat}.
Handle Missing Nutrients:

If any food item does not contain specific nutrient keys (calories, carbs, or fat), the function will default those values to 0 during the summation.
Test with Different Inputs:

You can test the function with various inputs, including:
Normal cases with all nutrient values present.
Cases where some nutrients are missing.
An empty list to ensure it returns zeroes for all nutrients.
Use the Results:

Utilize the aggregated nutrient totals for dietary tracking, meal planning, or nutritional analysis.


### Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![1](./visual_design.png)

![2](./visual_design.png)


---
