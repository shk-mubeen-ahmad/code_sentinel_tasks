import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")

print("Dataset loaded!")
print("Number of rows and columns:", df.shape)
print("\nColumns in dataset:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values in each column:")
print(df.isnull().sum())

# Handle missing values
if 'age' in df.columns:
    df['age'] = df['age'].fillna(df['age'].median())

if 'fare' in df.columns:
    df['fare'] = df['fare'].fillna(df['fare'].median())

# Encode categorical columns
if 'sex' in df.columns:
    df['sex'] = df['sex'].map({'male': 1, 'female': 0})

print("\nMissing values after fixing:")
print(df.isnull().sum())

print("\nFirst 5 rows after preprocessing:")
print(df.head())
