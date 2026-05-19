import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_dataset.csv")

df['visit_date'] = pd.to_datetime(df['visit_date'])

reference_date = df['visit_date'].max()

rfm = df.groupby('customer_id').agg({
    'visit_date': lambda x: (reference_date - x.max()).days,
    'session_id': 'count',
    'revenue': 'sum'
}).reset_index()

rfm.columns = ['customer_id', 'Recency', 'Frequency', 'Monetary']

rfm['R_Score'] = pd.qcut(
    rfm['Recency'],
    5,
    labels=[5,4,3,2,1],
    duplicates='drop'
)

rfm['F_Score'] = pd.qcut(
    rfm['Frequency'].rank(method='first'),
    5,
    labels=[1,2,3,4,5],
    duplicates='drop'
)

rfm['M_Score'] = pd.qcut(
    rfm['Monetary'].rank(method='first'),
    5,
    labels=[1,2,3,4,5],
    duplicates='drop'
)

rfm['RFM_Score'] = (
    rfm['R_Score'].astype(str) +
    rfm['F_Score'].astype(str) +
    rfm['M_Score'].astype(str)
)

def segment_customer(row):

    if row['RFM_Score'] == '555':
        return 'High Value Customer'

    elif int(row['R_Score']) >= 4 and int(row['F_Score']) >= 3:
        return 'Potential Loyalist'

    elif int(row['R_Score']) <= 2:
        return 'At Risk Customer'

    else:
        return 'Regular Customer'

rfm['Customer_Segment'] = rfm.apply(
    segment_customer,
    axis=1
)

print("\n========== RFM ANALYSIS ==========\n")
print(rfm.head())

segment_counts = rfm['Customer_Segment'].value_counts()

print("\n========== CUSTOMER SEGMENTS ==========\n")
print(segment_counts)

plt.figure(figsize=(8,6))

plt.bar(
    segment_counts.index,
    segment_counts.values
)

plt.title("Customer Segmentation based on RFM")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("rfm_customer_segments.png")

plt.show()

rfm.to_csv("rfm_analysis_output.csv", index=False)

print("\n✅ RFM Analysis Completed Successfully")
print("✅ RFM Output Saved")