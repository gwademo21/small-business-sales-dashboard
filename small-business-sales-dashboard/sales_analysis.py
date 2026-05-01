import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders if they do not already exist
os.makedirs("data", exist_ok=True)
os.makedirs("visuals", exist_ok=True)

# -----------------------------
# Step 1: Create sample sales data
# -----------------------------

data = {
    "Date": [
        "2024-01-05", "2024-01-12", "2024-01-20",
        "2024-02-03", "2024-02-14", "2024-02-25",
        "2024-03-02", "2024-03-15", "2024-03-28",
        "2024-04-06", "2024-04-17", "2024-04-29",
        "2024-05-08", "2024-05-19", "2024-05-30",
        "2024-06-04", "2024-06-16", "2024-06-27"
    ],
    "Product": [
        "Hoodie", "T-Shirt", "Hat",
        "Hoodie", "Backpack", "T-Shirt",
        "Hat", "Hoodie", "Backpack",
        "T-Shirt", "Hat", "Hoodie",
        "Backpack", "T-Shirt", "Hat",
        "Hoodie", "Backpack", "T-Shirt"
    ],
    "Category": [
        "Apparel", "Apparel", "Accessories",
        "Apparel", "Accessories", "Apparel",
        "Accessories", "Apparel", "Accessories",
        "Apparel", "Accessories", "Apparel",
        "Accessories", "Apparel", "Accessories",
        "Apparel", "Accessories", "Apparel"
    ],
    "Units_Sold": [
        15, 30, 22,
        18, 10, 27,
        25, 21, 14,
        35, 28, 24,
        17, 32, 30,
        26, 20, 38
    ],
    "Price": [
        45, 22, 18,
        45, 60, 22,
        18, 45, 60,
        22, 18, 45,
        60, 22, 18,
        45, 60, 22
    ],
    "Cost": [
        24, 10, 7,
        24, 35, 10,
        7, 24, 35,
        10, 7, 24,
        35, 10, 7,
        24, 35, 10
    ],
    "Location": [
        "Logan", "Logan", "Ogden",
        "Salt Lake City", "Logan", "Ogden",
        "Logan", "Salt Lake City", "Ogden",
        "Logan", "Salt Lake City", "Logan",
        "Ogden", "Salt Lake City", "Logan",
        "Ogden", "Logan", "Salt Lake City"
    ]
}

df = pd.DataFrame(data)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create new calculated columns
df["Revenue"] = df["Units_Sold"] * df["Price"]
df["Total_Cost"] = df["Units_Sold"] * df["Cost"]
df["Profit"] = df["Revenue"] - df["Total_Cost"]
df["Month"] = df["Date"].dt.strftime("%B")

# Save the dataset
df.to_csv("data/sales_data.csv", index=False)

# -----------------------------
# Step 2: Basic analysis
# -----------------------------

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_units = df["Units_Sold"].sum()

top_product = df.groupby("Product")["Revenue"].sum().idxmax()
top_location = df.groupby("Location")["Revenue"].sum().idxmax()

print("Small Business Sales Dashboard Summary")
print("--------------------------------------")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Units Sold: {total_units}")
print(f"Top Product by Revenue: {top_product}")
print(f"Top Location by Revenue: {top_location}")

# -----------------------------
# Step 3: Create visuals
# -----------------------------

# Revenue by month
monthly_revenue = df.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(8, 5))
monthly_revenue.plot(kind="bar")
plt.title("Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("visuals/revenue_by_month.png")
plt.close()

# Revenue by product
product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
product_revenue.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("visuals/revenue_by_product.png")
plt.close()

# Profit by category
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("visuals/profit_by_category.png")
plt.close()

# Revenue by location
location_revenue = df.groupby("Location")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
location_revenue.plot(kind="bar")
plt.title("Revenue by Location")
plt.xlabel("Location")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("visuals/revenue_by_location.png")
plt.close()

print("\nCharts saved in the visuals folder.")
print("Dataset saved in the data folder.")