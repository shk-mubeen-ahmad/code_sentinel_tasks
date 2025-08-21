import pandas as pd

# Load dataset
df = pd.read_csv("iris.csv")

# Print column names
print("Column Names:")
print(df.columns.tolist())

# Print number of rows
print("\nNumber of Rows:", len(df))

# Print summary statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))
