import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_dataset.csv")

location_sales = df.groupby('location').agg(
    total_orders=('session_id', 'count'),
    total_revenue=('revenue', 'sum')
).reset_index()

location_sales = location_sales.sort_values(
    by='total_revenue',
    ascending=False
)

top_locations = location_sales.head(5)

low_locations = location_sales.tail(5)

print("\n========== TOP 5 LOCATIONS ==========\n")
print(top_locations)

print("\n========== LOWEST 5 LOCATIONS ==========\n")
print(low_locations)

category_location = df.groupby(
    ['location', 'product_category']
)['revenue'].sum().reset_index()

print("\n========== CATEGORY PERFORMANCE BY LOCATION ==========\n")
print(category_location.head())

plt.figure(figsize=(12,6))

plt.bar(
    top_locations['location'].astype(str),
    top_locations['total_revenue']
)

plt.title("Top Performing Locations")
plt.xlabel("Location")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("top_locations_bar_chart.png")

plt.show()

plt.figure(figsize=(12,6))

plt.bar(
    low_locations['location'].astype(str),
    low_locations['total_revenue']
)

plt.title("Low Performing Locations")
plt.xlabel("Location")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("low_locations_bar_chart.png")

plt.show()

heatmap_data = df.pivot_table(
    values='revenue',
    index='location',
    columns='visit_month',
    aggfunc='sum'
)

plt.figure(figsize=(14,8))

plt.imshow(heatmap_data, aspect='auto')

plt.colorbar(label='Revenue')

plt.title("Geographic Sales Heatmap")
plt.xlabel("Month")
plt.ylabel("Location")

plt.savefig("geographic_heatmap.png")

plt.show()

print("\n✅ Geographic Sales Performance Analysis Completed")
print("✅ Charts Generated Successfully")