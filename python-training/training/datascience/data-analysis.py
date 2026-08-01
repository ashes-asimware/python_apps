import pandas as pd

df_nba = pd.read_csv("data\\nba.csv")

print(f"Before: {df_nba.isnull().sum()}\n")

df_nba["Name"] = df_nba["Name"].fillna("No Name")
df_nba["Team"] = df_nba["Team"].fillna("No Team")
df_nba["Number"] = df_nba["Number"].fillna(-1)
df_nba["Position"] = df_nba["Position"].fillna("No Position")
df_nba["Age"] = df_nba["Age"].fillna(0)
df_nba["Height"] = df_nba["Height"].fillna(0)
df_nba["Weight"] = df_nba["Weight"].fillna(0)
df_nba["College"] = df_nba["College"].fillna("No College")

df_nba["Salary"] = df_nba["Salary"].fillna(0)

average_salary = df_nba["Salary"].replace(0, pd.NA).mean()
df_nba["Salary"] = df_nba["Salary"].replace(0, average_salary)

print(f"After: {df_nba.isnull().sum()}")

writer = pd.ExcelWriter("data\\nba_cleaned.xlsx", engine="xlsxwriter")

