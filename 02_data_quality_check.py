import pandas as pd
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Load dataset
file_path = project_folder / "data" / "bank_churn_dataset.csv"
df = pd.read_csv(file_path)

# Categorical columns
categorical_columns = [
    "gender",
    "occupation",
    "origin_province",
    "married",
    "active_member",
    "exit",
    "customer_segment",
    "loyalty_level",
    "digital_behavior",
    "risk_segment"
]

print("\n--- UNIQUE VALUES IN CATEGORICAL COLUMNS ---")

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].value_counts())

# Numerical summary
print("\n--- NUMERICAL SUMMARY ---")
print(df.describe().T)

print("\n--- KEY CUSTOMER CATEGORIES ---")

columns_to_check = [
    "gender",
    "married",
    "active_member",
    "exit",
    "customer_segment"
]

for column in columns_to_check:
    print(f"\n{column}:")
    print(df[column].value_counts())

print("\n--- DATE COLUMN CHECK ---")

date_columns = [
    "created_date",
    "last_active_date",
    "last_transaction_month"
]

for column in date_columns:
    print(f"\n{column}:")
    print("Data type:", df[column].dtype)
    print("First 5 values:")
    print(df[column].head().to_list())
    print("Unique values:", df[column].nunique())

print("\n--- LAST TRANSACTION MONTH CHECK ---")

print("First 20 values:")
print(df["last_transaction_month"].head(20).to_list())

print("\nSmallest values:")
print(df["last_transaction_month"].nsmallest(20).to_list())

print("\nLargest values:")
print(df["last_transaction_month"].nlargest(20).to_list())