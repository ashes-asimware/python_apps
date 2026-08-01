import pandas as pd
import random

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
product_list = [random.choice(products) for _ in range(sample_size)]
data = {
    "Product": [p.split(" (")[0] for p in product_list],
    "Category": [categories[p.split(" (")[1][0]] for p in product_list],
    "Quantity": [random.randint(1, 100) for _ in range(sample_size)],
}
df_products = pd.DataFrame(data)
pivot = df_products.pivot_table(
    index="Category",
    values="Quantity",
    aggfunc=["sum", "mean", "max"],
    fill_value=-1,
)
print(pivot)
