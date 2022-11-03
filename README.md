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
 #   Column                       Non-Null Count   Dtype  
---  ------                       --------------   -----  
 0   id                           693071 non-null  object 
 1   timestamp                    693071 non-null  float64
 2   hour                         693071 non-null  int64  
 3   day                          693071 non-null  int64  
 4   month                        693071 non-null  int64  
 5   datetime                     693071 non-null  object 
 6   timezone                     693071 non-null  object 
 7   source                       693071 non-null  object 
 8   destination                  693071 non-null  object 
 9   cab_type                     693071 non-null  object 
 10  product_id                   693071 non-null  object 
 11  name                         693071 non-null  object 
 12  price                        637976 non-null  float64
 13  distance                     693071 non-null  float64
 14  surge_multiplier             693071 non-null  float64
 15  latitude                     693071 non-null  float64
 16  longitude                    693071 non-null  float64
 17  temperature                  693071 non-null  float64
 18  apparentTemperature          693071 non-null  float64
 19  short_summary                693071 non-null  object 
 20  long_summary                 693071 non-null  object 
 21  precipIntensity              693071 non-null  float64
 22  precipProbability            693071 non-null  float64
 23  humidity                     693071 non-null  float64
 24  windSpeed                    693071 non-null  float64
 25  windGust                     693071 non-null  float64
 26  windGustTime                 693071 non-null  int64  
 27  visibility                   693071 non-null  float64
 28  temperatureHigh              693071 non-null  float64
 29  temperatureHighTime          693071 non-null  int64  
 30  temperatureLow               693071 non-null  float64
 31  temperatureLowTime           693071 non-null  int64  
 32  apparentTemperatureHigh      693071 non-null  float64
 33  apparentTemperatureHighTime  693071 non-null  int64  
 34  apparentTemperatureLow       693071 non-null  float64
 35  apparentTemperatureLowTime   693071 non-null  int64  
 36  icon                         693071 non-null  object 
 37  dewPoint                     693071 non-null  float64
 38  pressure                     693071 non-null  float64
 39  windBearing                  693071 non-null  int64  
 40  cloudCover                   693071 non-null  float64
 41  uvIndex                      693071 non-null  int64  
 42  visibility.1                 693071 non-null  float64
 43  ozone                        693071 non-null  float64
 44  sunriseTime                  693071 non-null  int64  
 45  sunsetTime                   693071 non-null  int64  
 46  moonPhase                    693071 non-null  float64
 47  precipIntensityMax           693071 non-null  float64
 48  uvIndexTime                  693071 non-null  int64  
 49  temperatureMin               693071 non-null  float64
 50  temperatureMinTime           693071 non-null  int64  
 51  temperatureMax               693071 non-null  float64
 52  temperatureMaxTime           693071 non-null  int64  
 53  apparentTemperatureMin       693071 non-null  float64
 54  apparentTemperatureMinTime   693071 non-null  int64  
 55  apparentTemperatureMax       693071 non-null  float64
 56  apparentTemperatureMaxTime   693071 non-null  int64  
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
- 
![image](https://user-images.githubusercontent.com/90852026/199748586-536efad2-319e-4e5f-b2de-0ba5bfc168b3.png)
- There is no significant difference from the use of Uber and Lyft
- 
![image](https://user-images.githubusercontent.com/90852026/199748849-94afca5d-ba2d-4b60-8303-9e2d2014a9f7.png)
- Destination Uber and Lyft by Distance
- 
![image](https://user-images.githubusercontent.com/90852026/199749174-d2bc457e-e144-4577-a4ac-fe9c65d4139d.png)
- Outlier data Price vs Cab Type
- 
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
