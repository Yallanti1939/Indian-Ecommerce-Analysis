import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_dataset.csv")

top_products = df.groupby('product_id').agg(
    total_quantity=('quantity', 'sum'),
    total_revenue=('revenue', 'sum')
).reset_index()

top_products = top_products.sort_values(
    by='total_revenue',
    ascending=False
)

top_10_products = top_products.head(10)

print("\n========== TOP 10 PRODUCTS ==========\n")
print(top_10_products)

top_categories = df.groupby('product_category').agg(
    total_quantity=('quantity', 'sum'),
    total_revenue=('revenue', 'sum')
).reset_index()

top_categories = top_categories.sort_values(
    by='total_revenue',
    ascending=False
)

top_10_categories = top_categories.head(10)

print("\n========== TOP CATEGORIES ==========\n")
print(top_10_categories)

best_product = top_products.iloc[0]
low_product = top_products.iloc[-1]

print("\n========== BEST SELLING PRODUCT ==========\n")
print(best_product)

print("\n========== LOWEST SELLING PRODUCT ==========\n")
print(low_product)

plt.figure(figsize=(12,6))

plt.bar(
    top_10_products['product_id'].astype(str),
    top_10_products['total_revenue']
)

plt.title("Top 10 Best-Selling Products")
plt.xlabel("Product ID")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("top_products_bar_chart.png")

plt.show()

plt.figure(figsize=(12,6))

plt.bar(
    top_10_categories['product_category'].astype(str),
    top_10_categories['total_revenue']
)

plt.title("Top Product Categories")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("top_categories_bar_chart.png")

plt.show()

plt.figure(figsize=(8,8))

plt.pie(
    top_10_categories['total_revenue'],
    labels=top_10_categories['product_category'].astype(str),
    autopct='%1.1f%%'
)

plt.title("Revenue Distribution by Category")

plt.savefig("category_pie_chart.png")

plt.show()

seasonal_sales = df.groupby(
    ['visit_month', 'product_category']
)['revenue'].sum().reset_index()

print("\n========== SEASONAL CATEGORY SALES ==========\n")
print(seasonal_sales.head())

print("\n✅ Best-Selling Product Analysis Completed")
print("✅ Charts Generated Successfully")