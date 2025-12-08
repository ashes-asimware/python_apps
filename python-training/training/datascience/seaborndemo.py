import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set(style="white")
rs = np.random.RandomState(10)
d = rs.normal(size=100)
sns.histplot(d, kde=True, color="m")

data = pd.DataFrame(
    {"Year": [2018, 2019, 2020, 2021, 2022], "Sales": [100, 150, 200, 250, 300]}
)

plt.figure(figsize=(8, 5))
sns.lineplot(x="Year", y="Sales", data=data, marker="o")
plt.title("Yearly Sales Growth", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle="--")
plt.show()

x = np.linspace(0, 10, 20)
y = np.sin(x)
plt.figure(figsize=(8, 5))
sns.lineplot(x=x, y=y, color="b", label="Sine Wave")
plt.scatter(x, y, color="r", marker="o", label="Data Points")
plt.title("Seaborn Scatter plot with Matplot", fontsize=14, fontweight="bold")
plt.xlabel("X values", fontsize=12)
plt.ylabel("Y values", fontsize=12)
plt.legend()
plt.show()

dataset = pd.read_csv(r"data\graph_data.csv")
sns.kdeplot(dataset["Age"], color="g", shade=True)
plt.title("Age Distribution", fontsize=14, fontweight="bold")
plt.figure()
plt.show()

highnumber = dataset.Age[(dataset.Age >= 20) & (dataset.Age <= 40)].count()
sns.kdeplot(dataset, x="Age", y="Fare", fill=True)

total = dataset.query("100<=Fare<=200 and 20<=Age<=40")["Age"].count()

sns.kdeplot(
    x=dataset[dataset.Gender == "Female"]["Age"],
    fill=False,
    color="blue",
    label="Female",
)
sns.kdeplot(
    x=dataset[dataset.Gender == "Male"]["Age"], fill=False, color="orange", label="Male"
)
plt.title("Age Distribution by Gender", fontsize=14, fontweight="bold")
plt.legend()
plt.show()
