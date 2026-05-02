# Small Business Sales Dashboard

## Project Overview

This project analyzes sales data for a fictional small business. The goal is to identify revenue trends, top-selling products, profitable categories, and strong sales locations.

## Business Problem

Small businesses often collect sales data but do not always know how to turn that data into useful decisions. This dashboard helps answer:

- Which products generate the most revenue?
- Which months have the strongest sales?
- Which categories are most profitable?
- Which locations perform the best?

---

## Tools Used

- Python
- Pandas
- Matplotlib
- VS Code
- GitHub

---

## Dataset

A fictional dataset was created for this project containing:

- Date
- Product
- Category
- Units Sold
- Price
- Cost
- Location
- Revenue (calculated)
- Profit (calculated)
- Month (derived)

---

## Analysis Process

1. Created a structured sales dataset
2. Loaded and cleaned data using Pandas
3. Created calculated fields (Revenue, Cost, Profit)
4. Grouped data by:
   - Month
   - Product
   - Category
   - Location
5. Built visualizations using Matplotlib
6. Generated business insights and recommendations

---

## Key Findings

- Total revenue was $13,794.
- Total profit was $6,808.
- Hoodies generated the most revenue.
- Logan was the top location by revenue.
- Apparel category generated the highest overall revenue.

---

##  Business Insights

- High-performing products (like Hoodies) should be prioritized in inventory and marketing
- Sales trends vary by month, allowing better planning for promotions
- Certain locations outperform others and should receive more focus
- Some lower-revenue products may still be valuable due to higher margins

---

## How a Small Business Could Use This

A business owner could use this dashboard to:

- Identify top-selling products to restock
- Plan promotions around high-performing months
- Focus marketing on top-performing locations
- Improve profitability by promoting high-margin items
- Monitor overall business performance over time

---

## Visualizations

### Revenue by Month
![Revenue by Month](visuals/revenue_by_month.png)

### Revenue by Product
![Revenue by Product](visuals/revenue_by_product.png)

### Profit by Category
![Profit by Category](visuals/profit_by_category.png)

### Revenue by Location
![Revenue by Location](visuals/revenue_by_location.png)

## How to Run This Project

```bash
git clone https://github.com/gwademo21/small-business-sales-dashboard.git
pip install -r requirements.txt
python sales_analysis.py