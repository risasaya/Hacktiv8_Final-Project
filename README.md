# Hacktiv8_Final-Project
 This repository contains the final project of the Independent Data Science Study at Hacktiv8

## Final Project 1 : Uber and Lyft Price Prediction using Linear Regression

### Use Case 
Analyze factors affecting the dynamic pricing and the difference between Uber and Lyft special prices.
- Objective Statement : Implement Linear Regression to make uber and lyft price predictions.
- Challeges :
 - Large size of data.
 - Need several coordination from each department.
 - Many columns that are not correlated with the target feature.
- Methodology / Analytic Technique: Descriptive analysis

### Dataset
RangeIndex: 693071 entries, 0 to 693070
Data columns (total 57 columns):
dtypes: float64(29), int64(17), object(11)
memory usage: 301.4+ MB

### Data preparation
Python Version: 3.7.6
Packages: Pandas, Numpy, Matplotlib, Seaborn, and Sklearn.

### Data Cleansing
- No duplicate data
- Missing value on column price
- Duplicate column visibility

### Exploratory Data Analysis
- Average price of Uber and Lyft

![image](https://user-images.githubusercontent.com/90852026/199748586-536efad2-319e-4e5f-b2de-0ba5bfc168b3.png)
- There is no significant difference from the use of Uber and Lyft

![image](https://user-images.githubusercontent.com/90852026/199748849-94afca5d-ba2d-4b60-8303-9e2d2014a9f7.png)
- Destination Uber and Lyft by Distance

![image](https://user-images.githubusercontent.com/90852026/199749174-d2bc457e-e144-4577-a4ac-fe9c65d4139d.png)
- Outlier data Price vs Cab Type

![image](https://user-images.githubusercontent.com/90852026/199749319-d83d9b6f-8020-4fd7-b0b4-8e1ab5ac53fe.png)
- Price analysis :
 - Average or mean of price data in every route (source-destination)
 - Maximum price data : 97.5
 - Financial District - Fenway' route (by lyft) costs 97.5 dollars, which is our maximum price data

### Data Preprocessing
- Removing Unnecessary Features
- Check the correlation of temperature related features with target feature (Price)
- Check the correlation of cilmate related features with target feature (Price)
- Check categorical value in dataset features
- Check the correlation of categorical features with target feature (price)
- Drop the features have weak correlation with target feature (price)
- Remove Outliers using IQR metho

### Modelling Data : Linear Regression
- Encoding Data (One Hot Encoding)
- Dataset Split 7:3 
- Accuracy score : 93,37%
- MSE : 5.108258511106602
- RMSE : 2.2601456836024094

### Recommendation : 
There are still better and more accurate models than Linear Regression. Use the best model when dealing with real data.


## Final Project 2 : Coming Soon
