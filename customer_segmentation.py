import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("rfm_analysis_output.csv")

def customer_segment(row):

    r = int(row['R_Score'])
    f = int(row['F_Score'])
    m = int(row['M_Score'])

    if r >= 4 and f >= 4 and m >= 4:
        return "High-Value Customer"

    elif r >= 4 and f >= 3:
        return "Potential Loyalist"

    elif r <= 2 and f >= 3:
        return "At-Risk Customer"

    elif r >= 4 and f <= 2:
        return "New Customer"

    elif r <= 2 and f <= 2:
        return "Lost Customer"

    else:
        return "Regular Customer"

df['Customer_Segment'] = df.apply(
    customer_segment,
    axis=1
)

print("\n========== CUSTOMER SEGMENTS ==========\n")
print(df[['customer_id', 'RFM_Score', 'Customer_Segment']].head())

segment_counts = df['Customer_Segment'].value_counts()

print("\n========== SEGMENT COUNTS ==========\n")
print(segment_counts)

segment_revenue = df.groupby(
    'Customer_Segment'
)['Monetary'].sum().reset_index()

print("\n========== SEGMENT REVENUE ==========\n")
print(segment_revenue)

plt.figure(figsize=(10,6))

plt.bar(
    segment_counts.index,
    segment_counts.values
)

plt.title("Customer Segments Distribution")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("customer_segments_bar_chart.png")

plt.show()

plt.figure(figsize=(8,8))

plt.pie(
    segment_counts.values,
    labels=segment_counts.index,
    autopct='%1.1f%%'
)

plt.title("Customer Segments Pie Chart")

plt.savefig("customer_segments_pie_chart.png")

plt.show()

plt.figure(figsize=(8,6))

plt.scatter(
    df['Frequency'],
    df['Monetary']
)

plt.title("Frequency vs Monetary Value")
plt.xlabel("Frequency")
plt.ylabel("Monetary Value")

plt.tight_layout()

plt.savefig("rfm_scatter_plot.png")

plt.show()

df.to_csv("customer_segmented_output.csv", index=False)

print("\n✅ Customer Segmentation Completed Successfully")
print("✅ Segmented Dataset Saved")