import pandas as pd
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Load original dataset
input_file = project_folder / "data" / "bank_churn_dataset.csv"

df = pd.read_csv(input_file)

# Rename columns to clear, professional names
df = df.rename(columns={
    "credit_sco": "credit_score",
    "monthly_ir": "monthly_income",
    "tenure_ye": "tenure_years",
    "nums_card": "number_of_cards",
    "nums_service": "number_of_services",
    "last_transaction_month": "last_transaction_value"
})

# Convert date columns to proper date format
df["created_date"] = pd.to_datetime(
    df["created_date"],
    format="%d/%m/%Y"
)

df["last_active_date"] = pd.to_datetime(
    df["last_active_date"],
    format="%d/%m/%Y"
)

# Remove columns we don't need for analysis
df = df.drop(columns=["full_name", "address"])

# Save cleaned dataset
output_file = project_folder / "data" / "bank_churn_cleaned.csv"

df.to_csv(output_file, index=False)

print("Cleaning completed successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Saved to:", output_file)