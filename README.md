# Assignment 8 – Data Visualization with Seaborn

## Project Purpose

The purpose of this project is to use **Seaborn** to create visually appealing and informative data visualizations from real-world datasets. The goal is to explore patterns, relationships, and distributions in the data and clearly communicate insights through graphs.

This assignment focuses on:

- Importing and preparing data for visualization  
- Using Seaborn to create different types of plots  
- Comparing categories and relationships in datasets  
- Interpreting and explaining patterns found in the data  

Only the allowed libraries were used:

- `seaborn`
- `pandas`
- `numpy`
- standard Python modules  

---

## Datasets Used

### Exercise Dataset

This dataset contains information about **pulse rates** measured under different conditions:

- Diet types (e.g., no-fat diet)  
- Types of exercise (e.g., running)  
- Time intervals (1 min, 15 min, 30 min)  

The goal is to analyze how **diet and exercise impact heart rat**.

---

### Planets Dataset

This is a built-in dataset from Seaborn that contains information about discovered planets, including:

- Planet mass  
- Distance from Earth  
- Discovery method  
- Year discovered  

The goal is to explore patterns in planetary discoveries and characteristics.

---

## Class Design and Implementation

The program is organized using a class-based structure to keep the code clean and easy to follow. Each part of the assignment (data loading, visualization, and analysis) is handled separately.

### Main Class

`SeabornVisualizationAnalyzer`

This class is responsible for:

- loading datasets  
- preparing data for visualization  
- creating all required plots  
- printing analysis summaries  

This design improves organization and makes the code easier to maintain.

---

## Class Attributes

`exercise_data`  
Stores the exercise dataset loaded from CSV.

`planets_data`  
Stores the Seaborn planets dataset.

`pivot_table`  
Stores transformed exercise data used for creating the heatmap.

---

## Class Methods

`load_data()`  
Loads both the exercise dataset and the planets dataset.

`create_exercise_visualizations()`  
Creates visualizations for the exercise dataset:

- **Heatmap** showing average pulse across diet, exercise type, and time  
- **Categorical plots (boxplots)** showing pulse distributions by:
  - diet  
  - exercise type  

These plots help shpw how heart rate changes based on different conditions.

---

`create_planets_visualizations()`  
Creates six visualizations using the planets dataset:

### Relational Plots
- Scatter plot of planet mass vs distance  
- Line plot showing discovery trends over time  

### Distribution Plots
- Distribution of planet mass by discovery method  
- Distribution of orbital period  

### Categorical Plots
- Mass comparison across discovery methods  
- Count of planets discovered by method  

These plots highlight relationships, distributions, and category differences in the dataset.

---

`print_analysis()`  
Prints written conclusions based on both datasets.

---

## Visualization Summary

### Exercise Data Insights

- Pulse values increase over time during exercise  
- Running produces the highest pulse rates  
- Diet type slightly affects starting pulse levels  
- The heatmap clearly shows how pulse changes across time and conditions  

---

### Planets Data Insights

- Larger planets are often found at greater distances  
- Discovery methods vary widely in the number of planets found  
- Planet mass and orbital period show different distributions depending on detection method  

**Best visualization:**  
The **mass vs distance scatter plot** clearly shows relationships between planetary size and distance, making it the most effective at highlighting patterns.

---

## Limitations

Some limitations of this project include:

- Visualizations show trends but do not prove cause-and-effect relationships  
- Some datasets may contain missing or simplified data  
- Seaborn plots depend on proper data formatting and cleaning  
- No advanced statistical analysis was performed beyond visualization  
