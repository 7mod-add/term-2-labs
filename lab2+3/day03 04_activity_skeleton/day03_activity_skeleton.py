"""
Day 3 Activity: Use lambda and .apply() to clean a dataset.
Tasks:
1) Clean price (remove $ and commas)
2) Fill missing quantity with 0
3) Create total = price * quantity
4) Categorize price: low / med / high
"""

import pandas as pd

# Sample dataset
raw = {
    "product": ["Widget A", "Widget B", "Widget C"],
    "price": ["$1,234.50", "$567.89", "$2,345.00"],
    "quantity": [10, 5, None],
}

df = pd.DataFrame(raw)

# TODO: Clean price column using .apply with lambda.
df["price"]=df["price"].apply(
    lambda x: float(x.replace("$", "").replace(",", ""))
)
# TODO: Fill missing quantity with 0.
df["quantity"]=df["quantity"].apply(
    lambda x: 0 if pd.isna(x) else x
)
# TODO: Create total column.
df["total"]=df["price"]*df["quantity"]
# TODO: Add price_category column (low/med/high).
df["price_cat"]=df["price"].apply(
    lambda x: "low" if x<1000 else ("med" if x<2000 else "high")
)
print(df)
