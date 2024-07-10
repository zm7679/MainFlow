import pandas as pd

# Provide the full path to the CSV file
df = pd.read_csv('C:\Users\VENTAN\Downloads\MainFlow\Task 2\sales_data.csv')
print("Initial DataFrame:")
print(df.head())

# Step 2: Data Cleaning
# Handling missing values
print("\nMissing values before handling:")
print(df.isnull().sum())

df.fillna(0, inplace=True)
print("\nDataFrame after filling missing values:")
print(df.head())

# Removing duplicates
print("\nNumber of duplicate rows before removing:")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)
print("\nDataFrame after removing duplicates:")
print(df.head())

# Step 3: Data Manipulation
# Filtering data
filtered_df = df[df['quantity'] > 5]
print("\nFiltered DataFrame:")
print(filtered_df.head())

# Sorting data
sorted_df = df.sort_values(by='price', ascending=False)
print("\nSorted DataFrame:")
print(sorted_df.head())

# Grouping data
# Select only numeric columns for mean calculation
numeric_columns = df.select_dtypes(include=['number']).columns
grouped_df = df.groupby('product')[numeric_columns].mean()
print("\nGrouped DataFrame:")
print(grouped_df)
