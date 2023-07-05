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


## Final Project 3 : Cardiovascular Disease Prediction using Ensemble Model

### Use Case 
Predict the probability of Cardiovascular disease occurrence, based on a combination of features that describes the disease.
* Objective Statement : This project was created to evaluate the concept of Ensemble Model as follows:
  - Understand the concept of Classification with the Ensemble Model
  - Prepare data for use in the Ensemble Model
  - Implement the Ensemble Model to make predictions, and in this case predict whether someone will have a heart attack or not
* Challeges :
  - Imbalance dataset
  - Need several coordination from each department.
* Methodology / Analytic Technique: Descriptive analysis adn Graph Analysis

### Dataset
RangeIndex: 299 entries, 0 to 298 
Data columns (total 13 columns) 
dtypes: float64(3), int64(10) 
memory usage: 30.5 KB

### Data preparation
Python Version: 3.7.6
Packages: Pandas, Numpy, Matplotlib, Seaborn, and Sklearn.

### Data Cleansing
- No duplicate data
- No Missing value

### Exploratory Data Analysis
Outliers distribution using Histogram, Probability Plot, and Boxplot.
* Correlation between the age feature and the DEATH_EVENT label.

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/720431fb-36a4-4acf-82e7-86a878c4105f)

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/df93a7b9-d650-416b-91bd-2fc8311181b0)

* Correlation between sex feature and label DEATH_EVENT.

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/ea2f7196-445b-4f35-a1f3-b7f6207da95a)

* Correlation between time follow-up feature and label DEATH_EVENT.

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/9ca8ead7-80db-4b6c-b7a3-c4419d61920a)

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/f5a39e88-162f-4d99-b4d9-94c017048e56)

* Correlation between features of anemia, diabetes, high blood pressure, and smoking with the DEATH_EVENT label.

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/ce865e8d-9c3d-4b36-b7fc-2225b868fc47)

* Amount of creatinine_phosphokinase, ejection_fraction, platelets, serum_creatinine, or serum_sodium affects the heart attack

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/9721ab1e-c82a-43a7-a22b-61ee5d99286d)

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/28d51d0f-a952-4994-9dc1-aae45933471e)

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/acdabe1b-dbbb-4641-a80c-44f994cdad9c)

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/57144e9e-12e6-44af-8605-26dee3a23b1e)

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/4714f9fa-22e8-4e02-b2cd-9fb196007403)

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/75343166-b021-42a9-9bd5-b68c7b6b6b8d)

*Correlation matrix between all feature

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/c369820e-6f52-407b-a5a7-f259d4ea66be)

* Correlation difference between all feature

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/b80798ac-df4d-45e5-9a75-2dc8c10b089c)

* Cardiovascular Disease analysis :
  - The older a person is the possibility of dying from a heart attack is quite high.
  - Gender has little effect on heart failure
  - Time follow-up has an influence on heart failure
  - Features anemia, diabetes, high blood pressure, and smoking does not have a strong correlation with heart failure
  - Low amount of Creatinine Phosphokinase can reduce the chances of having a heart attack
  - Higher percentage of Ejection Fraction can reduce the chances of having a heart attack
  - Platelet count does not really affect the heart attack
  - The amount of Serum Creatinine that is above 1 mg/dL has a risk of having a heart attack
  - A low amount of Serum Sodium can increase the chances of having a heart attack
  - Features that are highly correlated with the target variable ('DEATH_EVENT') are age, ejection_fraction, serum_creatinine, and time

### Data Preprocessing
- Drop the features have weak correlation with target feature (DEATH_EVENT)
- Removing Unnecessary Features 
- Handle Imbalance Class using SMOTE
- Handle Skewness using Box-Cox
- Perform hyperparameter settings using RandomizedSearchCV

### Modelling Data : Random Forest Classifier

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/cf3f60f4-ebab-4cb3-a921-8976d95a9451)

* Without Oversampling
  - Dataset Split 80%:20%
  - Train Data Score: 0.9205020920502092
  - Test Data Score: 0.8333333333333334
  - Accuracy Score:  0.8333333333333334
  - Precision Score:  0.8
  - Recall Score:  0.631578947368421
  - F1-Score:  0.7058823529411765
  - The confusion matrix displays:
    1. True Positives (Actual Positive:1 and Predict Positive:1) - 38
    2. True Negatives (Actual Negative:0 and Predict Negative:0) - 12
    3. False Positives (Actual Negative:0 but Predict Positive:1) - 7
    4. False Negatives (Actual Positive:1 but Predict Negative:0) - 3

* Using Oversampling
  - Dataset Split 80%:20%
  - Train Data Score: 0.9320987654320988
  - Test Data Score: 0.8902439024390244
  - Accuracy Score:  0.8902439024390244
  - Precision Score:  0.8809523809523809
  - Recall Score:  0.9024390243902439
  - F1-Score:  0.8915662650602411
  - The confusion matrix displays:
    1. True Positives (Actual Positive:1 and Predict Positive:1) - 36
    2. True Negatives (Actual Negative:0 and Predict Negative:0) - 37
    3. False Positives (Actual Negative:0 but Predict Positive:1) - 4
    4. False Negatives (Actual Positive:1 but Predict Negative:0) - 5

### Modelling Data : Extra-Trees Classifier

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/100d4071-6af4-4b2b-99b3-3e1cc954e243)

* Without Oversampling
  - Dataset Split 80%:20%
  - Train Data Score: 0.8326359832635983
  - Test Data Score: 0.7833333333333333
  - Accuracy Score:  0.7833333333333333
  - Precision Score:  0.625
  - Recall Score:  0.7894736842105263
  - F1-Score:  0.6976744186046512
  - The confusion matrix displays:
    1. True Positives (Actual Positive:1 and Predict Positive:1) - 32
    2. True Negatives (Actual Negative:0 and Predict Negative:0) - 15
    3. False Positives (Actual Negative:0 but Predict Positive:1) - 4
    4. False Negatives (Actual Positive:1 but Predict Negative:0) - 9

* Using Oversampling
  - Dataset Split 80%:20%
  - Train Data Score: 0.8580246913580247
  - Test Data Score: 0.8536585365853658
  - Accuracy Score:  0.8536585365853658
  - Precision Score:  0.8918918918918919
  - Recall Score:  0.8048780487804879
  - F1-Score:  0.8461538461538461
  - The confusion matrix displays:
    1. True Positives (Actual Positive:1 and Predict Positive:1) - 37
    2. True Negatives (Actual Negative:0 and Predict Negative:0) - 33
    3. False Positives (Actual Negative:0 but Predict Positive:1) - 8
    4. False Negatives (Actual Positive:1 but Predict Negative:0) - 4

### Modelling Data : Gradient Boosting Classifier

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/30383f66-2ca1-47ef-956f-4139da256942)

* Without Oversampling
  - Dataset Split 80%:20%
  - Train Data Score: 0.9330543933054394
  - Test Data Score: 0.85
  - Accuracy Score:  0.85
  - Precision Score:  0.8571428571428571
  - Recall Score:  0.631578947368421
  - F1-Score:  0.7272727272727273
  - The confusion matrix displays:
    1. True Positives (Actual Positive:1 and Predict Positive:1) - 39
    2. True Negatives (Actual Negative:0 and Predict Negative:0) - 12
    3. False Positives (Actual Negative:0 but Predict Positive:1) - 7
    4. False Negatives (Actual Positive:1 but Predict Negative:0) - 2

* Using Oversampling
  - Dataset Split 80%:20%
  - Train Data Score: 0.9382716049382716
  - Test Data Score: 0.9024390243902439
  - Accuracy Score:  0.9024390243902439
  - Precision Score:  0.9230769230769231
  - Recall Score:  0.8780487804878049
  - F1-Score:  0.9
  - The confusion matrix displays:
    1. True Positives (Actual Positive:1 and Predict Positive:1) - 38
    2. True Negatives (Actual Negative:0 and Predict Negative:0) - 36
    3. False Positives (Actual Negative:0 but Predict Positive:1) - 5
    4. False Negatives (Actual Positive:1 but Predict Negative:0) - 3

### Modelling Data : AdaBoost Classifier

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/c3f5b4c6-20c5-424f-aeaa-fcf87ebfe69b)

* Without Oversampling
  - Dataset Split 80&:20%
  - Train Data Score: 0.8870292887029289
  - Test Data Score: 0.8166666666666667
  - Accuracy Score:  0.8166666666666667
  - Precision Score:  0.9
  - Recall Score:  0.47368421052631576
  - F1-Score:  0.6206896551724138
  - The confusion matrix displays:
    1. True Positives (Actual Positive:1 and Predict Positive:1) - 40
    2. True Negatives (Actual Negative:0 and Predict Negative:0) - 9
    3. False Positives (Actual Negative:0 but Predict Positive:1) - 10
    4. False Negatives (Actual Positive:1 but Predict Negative:0) - 1

* Using Oversampling
  - Dataset Split 80%:20%
  - Train Data Score: 0.8734567901234568
  - Test Data Score: 0.8414634146341463
  - Accuracy Score:  0.8414634146341463
  - Precision Score:  0.868421052631579
  - Recall Score:  0.8048780487804879
  - F1-Score:  0.8354430379746836
  - The confusion matrix displays:
    1. True Positives (Actual Positive:1 and Predict Positive:1) - 36
    2. True Negatives (Actual Negative:0 and Predict Negative:0) - 33
    3. False Positives (Actual Negative:0 but Predict Positive:1) - 8
    4. False Negatives (Actual Positive:1 but Predict Negative:0) - 5

* ROC CURVE without Oversampling

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/8bc5eef2-c50c-4524-b4e1-5e11edf9f4d9)

* ROC CURVE using Oversampling

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/5d9626d7-da36-4e6f-80e1-9f1a1c27078a)

### Summary

![image](https://github.com/risasaya/Hacktiv8_Final-Project/assets/90852026/97be12ff-1f36-4c0e-9b5b-cb13460d5bfe)

### Recommendation :
The Random Forest model is an algorithm used to predict the likelihood of having a heart attack. The use of Gradient Boosting, Extraa-trees, and AdaBoost models can be used as another alternative because they have good evaluation metric values.


## Final Project 3 : Cardiovascular Disease Prediction using Ensemble Model

