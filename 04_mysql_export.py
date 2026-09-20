import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent

input_file = project_folder / "data" / "bank_churn_cleaned.csv"
output_file = project_folder / "data" / "bank_churn_mysql.csv"

df = pd.read_csv(input_file)

# Remove characters that can cause problems during MySQL Workbench import
df = df.applymap(
    lambda x: x.encode("ascii", "ignore").decode("ascii")
    if isinstance(x, str) else x
)

# Save as UTF-8 with BOM for better compatibility with Windows tools
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("MySQL-ready CSV created successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Saved to:", output_file)