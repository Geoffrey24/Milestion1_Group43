# Software Design Document

## Project Name: Food NUTRITION 
## Group Number: 43

## Team members

| Student Number | Name           | 
|----------------|----------------|
| s5329877       | Geofrry Karuga |
| s5404089       | MOHAMMAD KHAN  | 
|       |     | 


<div style="page-break-after: always;"></div>



# Table of Contents

<!-- TOC -->
* [Table of Contents](#table-of-contents)
  * [1. System Vision](#1-system-vision)
    * [1.1 Problem Background](#11-problem-background)
    * [1.2 System capabilities/overview](#12-system-capabilitiesoverview)
    * [1.3	Potential Benefits](#13potential-benefits)
  * [2. Requirements](#2-requirements)
    * [2.1 User Requirements](#21-user-requirements)
    * [2.2	Software Requirements](#22software-requirements)
    * [2.3 Use Case Diagrams](#23-use-case-diagrams)
    * [2.4 Use Cases](#24-use-cases)
  * [3.	Software Design and System Components](#3-software-design-and-system-components-)
    * [3.1	Software Design](#31software-design)
    * [3.2	System Components](#32system-components)
      * [3.2.1 Functions](#321-functions)
      * [3.2.2 Data Structures / Data Sources](#322-data-structures--data-sources)
      * [3.2.3 Detailed Design](#323-detailed-design)
  * [4. User Interface Design](#4-user-interface-design)
    * [4.1 Structural Design](#41-structural-design)
    * [4.2	Visual Design](#42visual-design)
<!-- TOC -->


<div style="page-break-after: always;"></div>



## 1. System Vision

### 1.1 Problem Background

- Problem Identification: What problem does this system solve?
 
The system addresses the challenge of accessing, analyzing, and visualizing nutritional data. Currently, users struggle with finding reliable nutritional information, comparing nutritional values across different food items, and understanding complex data in an intuitive way. The application provides a solution that simplifies these tasks, making nutritional information more accessible and actionable.
- Dataset: What is the dataset used?

The system will utilize a comprehensive nutritional database that includes detailed information on various food items, their macronutrient and micronutrient content, daily recommended values, and other relevant data. This dataset may be sourced from public health databases, scientific publications, or custom-built by the development team.
- Data Input/Output: What kind of data input and output is required?

Input: Users will input data through searching for food items within the application, applying filters, and possibly uploading custom food data in formats like CSV.

Output: The system will produce visual representations such as pie charts, bar graphs, and detailed nutritional breakdowns. Users can export these visualizations and data summaries for further analysis or reporting.
- Target Users: Who will use the system, and why?

The primary users include nutritionists, dietitians, fitness enthusiasts, and health-conscious individuals. They will use the system to easily access and analyze nutritional data, enabling them to make informed dietary choices, create meal plans, and educate clients or themselves about nutrition.

### 1.2 System capabilities/overview

- System Functionality: What will the system do?

The system will allow users to search for food items, view detailed nutritional information, visualize nutrient breakdowns, filter foods by specific nutritional ranges, and categorize foods based on nutrient levels.
- Features and Functionalities: Describe the key features and functionalities of the system.

1) Food Search: Users can search for specific food items and retrieve detailed nutritional information.

2) Nutrition Breakdown: Users can visualize the breakdown of nutrients for a selected food item using pie charts and bar graphs.

3) Nutrition Range Filter: Users can filter food items based on specified nutritional ranges (e.g., calories, fat, protein).
4) Nutrition Level Filter: Users can categorize foods based on low, mid, and high nutritional content levels.
5) Additional Feature: The team will brainstorm and implement an innovative feature that enhances the application's utility, such as a meal planning tool or a comparison function between different food items.

### 1.3	Benefit Analysis

How will this system provide value or benefit?

The system will provide value by simplifying the process of nutritional analysis and visualization. It will help users make informed decisions about their diet and health, ultimately contributing to better nutritional education and healthier lifestyles. The user-friendly interface and comprehensive data visualization will make complex nutritional information accessible to a broader audience.

## 2. Requirements

### 2.1 User Requirements

* Detail how users are expected to interact with or use the program:

User Interaction: Users will interact with the system through a graphical user interface (GUI) that allows them to search for food items, apply filters, and generate visual reports. The system must be intuitive, with clear navigation and responsive design.

#### Functionalities from End-User Perspective:

* Narrative Description: Users will search for food items by name, apply filters to refine their search, and view detailed nutritional information in both textual and graphical formats.
* Listing of User Needs:
  
Need 1: The system must allow users to easily search for food items by name or category.

Need 2: The system must provide clear and detailed nutritional information for each food item.

Need 3: The system must offer visualization tools (e.g., pie charts, bar graphs) to help users understand the nutritional content of food items.

Need 4: The system must allow users to filter food items based on nutritional criteria such as calorie range, fat content, etc.

Need 5: The system must enable users to categorize and compare foods based on their nutritional content.

#### Fictional User Persona:
Name: Sarah, a Nutritionist

Role: Sarah is a professional nutritionist who needs to create meal plans for her clients. She uses the application to quickly find nutritional information and visualize the impact of different foods on overall diet quality.

Needs: Sarah needs a reliable and efficient tool to access accurate nutritional data, compare food items, and present this information to her clients in a comprehensible manner.

Usage Scenario: Sarah uses the application to search for specific food items, visualize their nutritional breakdown, and export this information for use in client reports.
### 2.2	Software Requirements
Define the functionality the software will provide. This section should list requirements formally, often using the word "shall" to describe functionalities.

 Functional Requirements:  
- R1.2: The program shall display detailed nutritional information for each selected food item.
- R1.3: The program shall generate visualizations such as pie charts and bar graphs representing the nutritional breakdown of selected food items.
- R1.4: The program shall enable users to filter food items based on nutritional ranges such as calories, fat, protein, etc.
- R1.5: The program shall allow users to categorize and compare food items based on low, mid, and high nutritional content levels.
- R1.6: The program shall allow users to export nutritional information and visualizations in PDF or image format.

### 2.3 Use Case Diagram
Provide a system-level Use Case Diagram illustrating all required features.

Example:  
![Use Case Diagram](./UCD.png)

### 2.4 Use Cases
Include at least 5 use cases, each corresponding to a specific function.


| Use Case ID    | UC-001                |
|----------------|-----------------------|
| Use Case Name  | Search for Food Items |
| Actors         | User                    |
| Description    | he user searches for a food item by entering its name in the search bar.                  |
| Flow of Events |The user enters a food item name in the search bar also The system retrieves and displays a list of matching food items.
| Alternate Flow | If no matching food items are found, the system notifies the user and suggests related items.                  |

| Use Case ID    | UC-002                                                              |
|----------------|---------------------------------------------------------------------|
| Use Case Name  | Visualize Nutrition Breakdown                                       |
| Actors         | User                                                                |
| Description    | The user visualizes the nutrient breakdown of a selected food item. |
| Flow of Events | The user selects a food item from the search results. The system displays a pie chart and bar graph representing the nutritional content of the food item.              |
| Alternate Flow | If the food item lacks complete nutritional data, the system provides a warning and displays available data.                                                                |

| Use Case ID    | UC-003                                                                                                                                                                                                        |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Apply Nutrition Range Filter                                                                                                                                                                                  |
| Actors         | User                                                                                                                                                                                                          |
| Description    | The user applies a filter to find foods within a specific nutritional range                                                                                                                                   |
| Flow of Events | The user selects the "Filter" option, The user specifies the desired nutritional range (e.g., calories between 100-200), The system filters the list of food items and displays those that meet the criteria. |
| Alternate Flow | If no food items meet the criteria, the system suggests adjusting the filter settings.                                                                                                                                                                                                          |

| Use Case ID    | UC-004                                                                                                                                                                                                |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Categorize Foods by Nutrition Level                                                                                                                                                                   |
| Actors         | User                                                                                                                                                                                                  |
| Description    | The user categorizes foods into low, mid, and high nutritional content levels.                                                                                                                        |
| Flow of Events | The user selects the "Categorize" option, The system categorizes food items based on predefined nutritional thresholds, The categorized foods are displayed in separate sections for easy comparison. |
| Alternate Flow | If a food item does not fit into any category, the system provides a custom category.                                                                                                                                                                                                  |

| Use Case ID    | UC-005                                                                                                                                                 |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Export Nutritional Data                                                                                                                                |
| Actors         | User                                                                                                                                                   |
| Description    | The user exports the nutritional data and visualizations for a selected food item.                                                                     
| Flow of Events | The user selects the "Export" option, The user chooses the export format (e.g., PDF, PNG), The system generates the file and provides a download link. |
| Alternate Flow | If there is an issue with generating the file, the system notifies the user and suggests troubleshooting steps                                                                                                                                                   |



## 3.	Software Design and System Components 

### 3.1	Software Design
Include a flowchart that illustrates how your software will operate.

Example:  
![Software Design](./software_design_flowchart.png)

### 3.2	System Components

#### 3.2.1 Functions
List all key functions within the software. For each function, provide:
- Description: Brief explanation of the function’s purpose.
- Input Parameters: List parameters, their data types, and their use.
- Return Value: Describe what the function returns.
- Side Effects: Note any side effects, such as changes to global variables or data passed by reference.

#### 3.2.2 Data Structures / Data Sources
List all data structures or sources used in the software. For each, provide:

- Type: Type of data structure (e.g., list, set, dictionary).
- Usage: Describe where and how it is used.
- Functions: List functions that utilize this structure.

#### 3.2.3 Detailed Design
Provide pseudocode or flowcharts for all functions listed in Section 3.2.1 that operate on data structures. For instance, include pseudocode or a flowchart for a custom searching function.


## 4. User Interface Design

### 4.1 Structural Design
Present a structural design, a hierarchy chart, showing the overall interface’s structure. Address:

- Structure: How will the software be structured?
- Information Grouping: How will information be organized?
- Navigation: How will users navigate through the software?
- Design Choices: Explain why these design choices were made.

Example:  
![Structural Design](./Structural_Design.png)

### 4.2	Visual Design
Include all wireframes or mock-ups of the interface. Provide a discussion, explanation, and justification for your design choices. Hand-drawn wireframes are acceptable.

- Interface Components: Clearly label all components.
- Screens/Menus: Provide wireframes for different screens, menus, and options.
- Design Details: Focus on the layout and size of components; color and graphics are not required. 

Example:  
![Visual Design](./visual_design.png)



