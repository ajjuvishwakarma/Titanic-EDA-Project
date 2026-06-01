
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

# Load Dataset
df = pd.read_csv('Titanic-Dataset.csv')
print("Dataset Loaded Successfully")

# Dataset information
print("\nDataset Information:")
print(df.info())

# Summary Statistics-
print("\nSummary Statistics:")
print(df.describe())

# Check missing values-
print("\nMissing Values:")
print(df.isnull().sum())

# Histogram(Age Distribution)

"""print("\nCreating Histogram...")
df["Age"].hist(bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Numbers of Pasangers")
plt.show()"""

# Exact Count
age_groups = pd.cut(df["Age"],
bins=[0,10,20,30,40,50,60,70,80])
print("\nAge Group Counts:")
print(age_groups.value_counts().sort_index())
"""
#Boxplot(Fare)
sns.boxplot(x=df["Fare"])
plt.title("Fare Boxplot")
plt.show() """

# Correlation Matrix
corr = df.corr(numeric_only=True)
print(corr)

# Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()