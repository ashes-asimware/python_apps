import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="notebook")
tips = sns.load_dataset("tips")
tips.head()

print("Rows, Columns", tips.shape)
print(tips.info())
print(tips.describe())

tips.isna().sum()

tips["tip_pct"] = (tips["tip"] / tips["total_bill"]) * 100
tips["tip_pct"].head()

tips["bill_size"] = np.where(
    tips["total_bill"] < 15,
    "Small",
    np.where(tips["total_bill"] < 30, "Medium", "Large"),
)
tips["bill_size"].value_counts()

plt.figure(figsize=(7, 4))
sns.histplot(tips, x="total_bill", bins=20, kde=True, color="skyblue")
plt.title("Total Bill Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Total Bill", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.show()

plt.figure(figsize=(7, 4))
sns.histplot(tips, x="tip_pct", bins=20, kde=True, color="skyblue")
plt.title("Tip Percentage Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Tip Percentage", fontsize=12)
plt.show()

plt.figure(figsize=(7, 4))
sns.countplot(x="day", data=tips)
plt.title("Count by Day", fontsize=14, fontweight="bold")
plt.xlabel("Day", fontsize=12)
plt.show()

plt.figure(figsize=(7, 4))
sns.countplot(x="time", data=tips)
plt.title("Count by Time of Day", fontsize=14, fontweight="bold")
plt.xlabel("Day", fontsize=12)
plt.show()

plt.figure(figsize=(7, 4))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", style="smoker")
plt.title("Total Bill vs Multiple", fontsize=14, fontweight="bold")
plt.xlabel("Total Bill", fontsize=12)
plt.ylabel("Tip", fontsize=12)
plt.show()

plt.figure(figsize=(7, 4))
sns.boxplot(data=tips, x="day", y="tip_pct")
plt.title("Tip Percentage by Day")
plt.show()

plt.figure(figsize=(7, 4))
sns.boxplot(data=tips, x="bill_size", y="tip_pct", order=["Small", "Medium", "Large"])
plt.title("Tip Percentage by Bill Size")
plt.show()

numeric_cols = ["total_bill", "tip", "tip_pct", "size"]
correlation_matrix = tips[numeric_cols].corr()
plt.figure(figsize=(7, 4))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix", fontsize=14, fontweight="bold")
plt.show()

sns.pairplot(tips[numeric_cols], diag_kind="kde", markers="+", plot_kws={"alpha": 0.6})
plt.show()
