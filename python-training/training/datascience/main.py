import pandas as pd
import random

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"],
}

# print(pd.DataFrame(data))

# give me name and city for row 0 and 2
df = pd.DataFrame(data)
# print(df.loc[[0, 2], ["name", "city"]])

# use iloc to get the same result
# print(df.iloc[[0, 2], [0, 2]])


fruits = ["apple", "banana", "cherry", "date"]
# use this list and create a random sample of 50 fruits using choice
sampled_fruits = random.choices(fruits, k=50)
# print(sampled_fruits)

# create a dictionary with product names, quantity and prices
# using the sampled_fruits list, create a dataframe with random quantities and prices for each fruit
# add category column with random categories from a list of fruits and vegetables
product_data = {
    "product": sampled_fruits,
    "category": [random.choice(["fruit", "vegetable"]) for _ in range(50)],
    "quantity": [random.randint(1, 10) for _ in range(50)],
    "amount": [round(random.uniform(0.5, 5.0), 2) for _ in range(50)],
}
df_products = pd.DataFrame(product_data)

pivot = df_products.pivot_table(
    index="category", values="amount", aggfunc=["mean", "median", "min"]
)
print(pivot)
