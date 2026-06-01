# Titanic Dataset - Exploratory Data Analysis (EDA)

## Project Overview
This project performs Exploratory Data Analysis (EDA) on the Titanic Dataset using Python. The objective is to understand the dataset, identify missing values, analyze feature distributions, detect outliers, and discover relationships between variables.

## Tools and Libraries Used
- Python
- Pandas
- Matplotlib
- Seaborn

## Dataset
Titanic Survival Prediction Dataset

File:
- Titanic-Dataset.csv

## Tasks Performed

### 1. Data Loading
- Loaded the Titanic dataset using Pandas.
- Verified dataset structure and dimensions.

### 2. Dataset Information
- Checked data types of all columns.
- Identified numerical and categorical features.

### 3. Summary Statistics
- Generated statistical summaries using `describe()`.
- Analyzed mean, median, minimum, and maximum values.

### 4. Missing Value Analysis
Missing values found:

| Column | Missing Values |
|----------|----------|
| Age | 177 |
| Cabin | 687 |
| Embarked | 2 |

### 5. Age Distribution Analysis
- Created a histogram of passenger ages.
- Most passengers were between 20 and 30 years old.

### 6. Fare Outlier Detection
- Used a boxplot to identify outliers in the Fare column.
- Observed several high-fare outliers.

### 7. Correlation Analysis
- Generated a correlation matrix.
- Analyzed relationships among numerical features.

### 8. Heatmap Visualization
- Created a heatmap to visualize correlations.
- Strong negative correlation observed between Pclass and Fare (-0.55).
- Positive correlation observed between Fare and Survival (0.26).

## Patterns, Trends and Anomalies

### Patterns
- Most passengers belonged to the 20–30 age group.
- Fare and Survival show a positive relationship.

### Trends
- Higher-class passengers generally paid higher fares.
- Survival chances were slightly higher for passengers with expensive tickets.

### Anomalies
- Large number of missing values in the Cabin column.
- Presence of fare outliers.

## Results
The EDA process helped understand the Titanic dataset and revealed important relationships among passenger class, fare, age, and survival.

