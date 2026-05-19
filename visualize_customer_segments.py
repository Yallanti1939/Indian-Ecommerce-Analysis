import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer_segmented_output.csv")

print("\n========== CUSTOMER SEGMENTS ==========\n")
print(df[['customer_id', 'Customer_Segment']].head())

segment_counts = df['Customer_Segment'].value_counts()

plt.figure(figsize=(10,6))

plt.bar(
    segment_counts.index,
    segment_counts.values
)

plt.title("Customer Segment Distribution")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("segment_distribution_bar_chart.png")

plt.show()

plt.figure(figsize=(8,6))

plt.scatter(
    df['Frequency'],
    df['Monetary']
)

plt.title("Frequency vs Monetary Value")
plt.xlabel("Frequency")
plt.ylabel("Monetary")

plt.tight_layout()

plt.savefig("rfm_scatter_plot_visualization.png")

plt.show()

heatmap_data = pd.crosstab(
    df['R_Score'],
    df['F_Score']
)

plt.figure(figsize=(8,6))

plt.imshow(heatmap_data, aspect='auto')

plt.colorbar(label='Customer Count')

plt.title("RFM Heatmap")
plt.xlabel("Frequency Score")
plt.ylabel("Recency Score")

plt.savefig("rfm_heatmap.png")

plt.show()

plt.figure(figsize=(8,8))

plt.pie(
    segment_counts.values,
    labels=segment_counts.index,
    autopct='%1.1f%%'
)

plt.title("Customer Segment Proportions")

plt.savefig("segment_pie_chart.png")

plt.show()

print("\n✅ Customer Segment Visualization Completed")
print("✅ Charts Generated Successfully")