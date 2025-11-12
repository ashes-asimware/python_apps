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

sample_size = 20
products = [
    "Apple (F)",
    "Banana (F)",
    "Carrot (V)",
    "Broccoli (V)",
    "Chicken (P)",
    "Fish (P)",
]
categories = {"F": "Fruit", "V": "Vegetable", "P": "Protein"}
# Create list of 50 products by randomly selecting from products
product_list = [random.choice(products) for _ in range(sample_size)]
# create dictionary with 3 keys - "Product", "Category", "Quantity"
# values of "Product" should be name without the category suffix
# values of "Category" should be full category name from categories dict
# values of "Quantity" should be random integer between 1 and 100
data = {
    "Product": [p.split(" (")[0] for p in product_list],
    "Category": [categories[p.split(" (")[1][0]] for p in product_list],
    "Quantity": [random.randint(1, 100) for _ in range(sample_size)],
}
df_products = pd.DataFrame(data)
print(df_products)

pivot = df_products.pivot_table(
    index="Category",
    values="Quantity",
    aggfunc=["sum", "mean", "max"],
    fill_value=-1,
)
print(pivot)
