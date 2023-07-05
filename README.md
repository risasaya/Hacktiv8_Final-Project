# Hacktiv8_Final-Project
 This repository contains the final project of the Independent Data Science Study at Hacktiv8

## Final Project 1 : Uber and Lyft Price Prediction using Linear Regression

### Use Case 
Analyze factors affecting the dynamic pricing and the difference between Uber and Lyft special prices.
* Objective Statement : Implement Linear Regression to make uber and lyft price predictions.
* Challeges :
  - Large size of data.
  - Need several coordination from each department.
  - Many columns that are not correlated with the target feature.
* Methodology / Analytic Technique: Descriptive analysis

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
* Average price of Uber and Lyft

![image](https://user-images.githubusercontent.com/90852026/199748586-536efad2-319e-4e5f-b2de-0ba5bfc168b3.png)
* There is no significant difference from the use of Uber and Lyft

![image](https://user-images.githubusercontent.com/90852026/199748849-94afca5d-ba2d-4b60-8303-9e2d2014a9f7.png)
* Destination Uber and Lyft by Distance

![image](https://user-images.githubusercontent.com/90852026/199749174-d2bc457e-e144-4577-a4ac-fe9c65d4139d.png)
* Outlier data Price vs Cab Type

![image](https://user-images.githubusercontent.com/90852026/199749319-d83d9b6f-8020-4fd7-b0b4-8e1ab5ac53fe.png)
* Price analysis :
  - Average or mean of price data in every route (source-destination)
  - Maximum price data : 97.5
  - Financial District - Fenway' route (by lyft) costs 97.5 dollars, which is our maximum price data

### Data Preprocessing
- Removing Unnecessary Features
- Check categorical value in dataset features
- Check the correlation of categorical features with target feature (price)
- Drop the features have weak correlation with target feature (price)
- Remove Outliers using IQR method

### Modelling Data : Linear Regression
- Encoding Data (One Hot Encoding)
- Dataset Split 7:3 
- Accuracy score : 93,37%
- MSE : 5.108258511106602
- RMSE : 2.2601456836024094

### Recommendation : 
There are still better and more accurate models than Linear Regression. Use the best model when dealing with real data.

### Try Prediction : https://h8-kelompok8-fp1.herokuapp.com/


## Final Project 2 : Rain Prediction using Logistic Regression and Support Vector Machine

### Use Case 
Predict rainfall by extracting hidden patterns from historical weather data.
* Objective Statement : This project was created to evaluate the concept of Logistic Regression and SVM as follows:
  - Understand the concept of Classification with Logistic Regression and SVM
  - Prepare data for use in Logistic Regression and SVM models
  - Implement Logistic Regression and SVM to make predictions
* Challeges :
  - Data have a lot missing values.
  - Need several coordination from each department.
  - Many columns that are correlated with the target feature.
* Methodology / Analytic Technique: Descriptive analysis adn Graph Analysis

### Dataset
RangeIndex: 145460 entries, 0 to 145459
Data columns (total 23 columns):
dtypes: float64(16), object(7)
memory usage: 25.5+ MB

### Data preparation
Python Version: 3.7.6
Packages: Pandas, Numpy, Matplotlib, Seaborn, and Sklearn.

### Data Cleansing
- No duplicate data
- Missing value on 21 column of 23 column. Then the categorical variable is filled with the mode value and the numerical variable is filled with the median value.

### Exploratory Data Analysis
* Class comparison of the target feature

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/1539a2f7-7e74-4936-add9-8c4f7bd32492)
* Rain distribution by location in Australia

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/4f40ea51-6a8b-4e4e-9ea7-aae33f934fc0)
* Average rainfall based on rain tomorrow

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/83082302-4fdf-4ef1-9b0f-6fa7e31cc92e)
* Rain analysis :
  - The area that often rains is in Portland.
  - The area that don't rain often are in Woomera.
  - Min temperature is -8.5
  - Max temperature is 48

### Data Preprocessing
- Encoding data
- Check categorical value in dataset features
- Check the correlation of categorical features with target feature (RainTomorrow)
- Drop the features have weak correlation with target feature (RainTomorrow)
- Removing Unnecessary Features

### Modelling Data : Logistic Regression
- Dataset Split 7:3
- Accuracy score : 83,48%
- ROC Area under Curve = 0.6940801944173254
  ![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/ce0a49e0-e4f5-4822-a8f4-37bcfed6147f)
- The confusion matrix displays:
  ![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/36ca1570-af49-49ca-8cf1-8054e05397fb)
  1. True Positives (Actual Positive:1 and Predict Positive:1) - 32179
  2. True Negatives (Actual Negative:0 and Predict Negative:0) - 4251
  3. False Positives (Actual Negative:0 but Predict Positive:1) - 5351
  4. False Negatives (Actual Positive:1 but Predict Negative:0) - 1857

### Modelling Data : Support Vector Machine
- Dataset use : 72730
- Dataset Split 7:3
- Accuracy score : 83.6%
- ROC Area under Curve = 0.6778760143332175
  ![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/1932622e-5536-44ec-a33c-e0246c8caca6)
- The confusion matrix displays:
  ![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/3700128b-ad52-4ff0-a0a8-8ea32bfda7d0)
  1. True Positives (Actual Positive:1 and Predict Positive:1) - 16338
  2. True Negatives (Actual Negative:0 and Predict Negative:0) - 1903
  3. False Positives (Actual Negative:0 but Predict Positive:1) - 2924
  4. False Negatives (Actual Positive:1 but Predict Negative:0) - 654

### Recommendation : 
Based on this, the selected model is Logistic Regression, because the model uses all the data for modeling, so the model is well trained.

### Try Prediction :  https://fp2-rainpredict.herokuapp.com/


## Final Project 3 : 
