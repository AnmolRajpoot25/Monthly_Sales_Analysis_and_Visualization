This project involves analyzing sales data over a 12-month period to gain insights into sales trends, the best-performing products, and the sales performance across different cities.

## Table of Contents
- [Project Description](#project-description)
- [Data Cleaning](#data-cleaning)
- [Data Analysis](#data-analysis)
- [Results](#results)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)

## Project Description
The goal of this project is to analyze sales data from a retail company to understand:
1. The best month for sales.
2. The city with the highest sales.
3. The best time to display advertisements for maximum engagement.
4. Products that are often sold together.
5. The most sold product and the relationship between product price and quantity sold.

## Data Cleaning
The data cleaning process involved:
- Merging 3 months of sales data into a single CSV file.
- Dropping rows with all NaN values.
- Removing rows with invalid 'Order Date'.
- Converting columns to appropriate data types.
- Handling missing and duplicated values.

## Data Analysis
The data analysis process included:
1. **Best Month for Sales**: Calculating total sales for each month.
2. **City with Highest Sales**: Summing sales grouped by city.
3. **Best Time for Advertisement**: Analyzing sales data to determine peak order hours.
4. **Products Sold Together**: Identifying products that are frequently bought together.
5. **Most Sold Product**: Analyzing product sales quantities and exploring the relationship between price and quantity sold.

## Results
### Best Month for Sales
- Visualization of total sales per month to identify the best month for sales.

### City with Highest Sales
- Bar chart showing sales distribution across different cities.

### Best Time for Advertisement
- Line plot showing the number of orders at each hour of the day.

### Products Sold Together
- Analysis of frequently sold together products using combinations and counting their occurrences.

### Most Sold Product
- Bar chart showing the quantity of each product sold.
- Combined bar and line chart showing the relationship between product price and quantity sold.

## Dependencies
- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- NumPy

## How to Run
1. Ensure you have the required dependencies installed.
2. Download the dataset and place it in the appropriate directory.
3. Run the script `data_science_project.py` to execute the data cleaning and analysis steps.
4. The results will be displayed through various plots and printed outputs in the console.
