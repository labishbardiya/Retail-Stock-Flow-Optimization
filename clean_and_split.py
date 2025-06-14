import pandas as pd

# Load the raw dataset
df = pd.read_csv("inventory_forecasting.csv")

# Basic cleaning
df = df.dropna(subset=["Date", "Store ID", "Product ID", "Inventory Level"])  # remove critical nulls
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
df["Holiday/Promotion"] = df["Holiday/Promotion"].fillna(0).astype(int)

# Unique dimension tables
stores_df = df[["Store ID", "Region"]].drop_duplicates().rename(columns={"Store ID": "store_id", "Region": "region"})
products_df = df[["Product ID", "Category"]].drop_duplicates().rename(columns={"Product ID": "product_id", "Category": "category"})
calendar_df = df[["Date", "Seasonality", "Weather Condition", "Holiday/Promotion"]].drop_duplicates()
calendar_df = calendar_df.rename(columns={
    "Date": "date",
    "Seasonality": "seasonality",
    "Weather Condition": "weather",
    "Holiday/Promotion": "is_holiday"
})

# Main transactions table
inventory_df = df.rename(columns={
    "Date": "date",
    "Store ID": "store_id",
    "Product ID": "product_id",
    "Inventory Level": "inventory_level",
    "Units Sold": "units_sold",
    "Units Ordered": "units_ordered",
    "Demand Forecast": "demand_forecast",
    "Price": "price",
    "Discount": "discount",
    "Competitor Pricing": "competitor_price"
})

# Save to cleaned CSVs (optional)
stores_df.to_csv("stores.csv", index=False)
products_df.to_csv("products.csv", index=False)
calendar_df.to_csv("calendar.csv", index=False)
inventory_df.to_csv("inventory_transactions.csv", index=False)

print("✅ Data cleaned and split into 4 tables.")
