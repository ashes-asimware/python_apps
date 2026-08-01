import os
import json
import pandas as pd
import openpyxl
from helpers import calculate_total, format_currency

print(f"Current Working Directory: {os.getcwd()}")

data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"{data_path} file exists.")
else:
    print(f"{data_path} file does not exist.")
    print("Please ensure you are running from sales-analysis/ directory.")

df = pd.read_csv(data_path)
print(df)
print(f"Shape: {df.shape[0]} rows and {df.shape[1]} columns")

df['total'] = calculate_total(df['quantity'], df['price'])
print(df)

os.makedirs("output", exist_ok=True)
output_path = "output/sales.json"
df.to_json(output_path, orient="records", lines=True)

df.to_excel("output/sales.xlsx", index=False)

# Using helper functions to format and display sales data including grand total
totals = []
for i, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

df['total'] = totals

print("Display sales data")
for i, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"Grand Total: {formatted_grand_total}")
