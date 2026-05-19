import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer_segmented_output.csv")

sales_df = pd.read_csv("cleaned_dataset.csv")

top_categories = sales_df.groupby(
    'product_category'
)['revenue'].sum().sort_values(
    ascending=False
).head(5)

print("\n========== TOP GROWTH CATEGORIES ==========\n")
print(top_categories)

top_locations = sales_df.groupby(
    'location'
)['revenue'].sum().sort_values(
    ascending=False
).head(5)

print("\n========== TOP SALES LOCATIONS ==========\n")
print(top_locations)

high_value_customers = df[
    df['Customer_Segment'] == 'High-Value Customer'
]

print("\n========== HIGH VALUE CUSTOMERS ==========\n")
print(high_value_customers.head())

at_risk_customers = df[
    df['Customer_Segment'] == 'At-Risk Customer'
]

print("\n========== AT RISK CUSTOMERS ==========\n")
print(at_risk_customers.head())

avg_revenue = sales_df['revenue'].mean()

print("\n========== AVERAGE REVENUE ==========\n")
print(avg_revenue)

plt.figure(figsize=(10,6))

top_categories.plot(kind='bar')

plt.title("Top Product Categories")
plt.xlabel("Product Category")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("business_top_categories.png")

plt.show()

plt.figure(figsize=(10,6))

top_locations.plot(kind='bar')

plt.title("Top Sales Locations")
plt.xlabel("Location")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("business_top_locations.png")

plt.show()

segment_counts = df['Customer_Segment'].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    segment_counts.values,
    labels=segment_counts.index,
    autopct='%1.1f%%'
)

plt.title("Customer Segments Distribution")

plt.savefig("business_customer_segments.png")

plt.show()

print("\n✅ Business Opportunity Analysis Completed")
print("✅ Charts Generated Successfully")