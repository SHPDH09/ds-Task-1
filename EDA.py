import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a DataFrame from the given data
data = {
    "Math_Score": [65, 64, 76, 80, 63, 73, 72, 77, 74, 68, 64, 75, 62, 69, 74],
    "Reading_Score": [86, 85, 77, 76, 91, 95, 82, 82, 90, 85, 78, 83, 89, 80, 84],
    "Writing_Score": [67, 71, 77, 75, 62, 62, 76, 62, 60, 72, 80, 76, 61, 73, 80],
    "Placement_Score": [78, 80, 84, 75, 90, 79, 79, 87, 100, 89, 84, 83, 76, 87, 79],
    "Club_Join_Date": [2021, 2019, 2021, 2021, 2019, 2020, 2020, 2021, 2019, 2019, 2019, 2019, 2019, 2021, 2019]
}

df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())

# Display the column names
print(df.columns)

# Understand the dataset
# Display basic information about the dataset
print(df.info())

# Display summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Visualize distributions
# Histograms
df.hist(bins=20, figsize=(10, 10))
plt.show()

# Boxplots
plt.figure(figsize=(12, 6))
sns.boxplot(data=df)
plt.show()

# After inspecting the column names, replace 'actual_categorical_column' with the correct column name
actual_categorical_column = 'Club_Join_Date'  # Use the new categorical column

# Pairplot to visualize pairwise relationships
sns.pairplot(df, hue=actual_categorical_column)
plt.show()

# Analyze relationships and correlations
# Scatter plot for Math Score vs Reading Score
sns.scatterplot(x='Math_Score', y='Reading_Score', hue=actual_categorical_column, data=df)
plt.show()

# Scatter plot for Reading Score vs Writing Score
sns.scatterplot(x='Reading_Score', y='Writing_Score', hue=actual_categorical_column, data=df)
plt.show()

# Drop non-numeric columns for correlation matrix
numeric_df = df[['Math_Score', 'Reading_Score', 'Writing_Score', 'Placement_Score']]

# Correlation heatmap
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Identify outliers using box plots
# Boxplot for Math Score
sns.boxplot(x=actual_categorical_column, y='Math_Score', data=df)
plt.show()

# Boxplot for Reading Score
sns.boxplot(x=actual_categorical_column, y='Reading_Score', data=df)
plt.show()

# Boxplot for Writing Score
sns.boxplot(x=actual_categorical_column, y='Writing_Score', data=df)
plt.show()

# Boxplot for Placement Score
sns.boxplot(x=actual_categorical_column, y='Placement_Score', data=df)
plt.show()
