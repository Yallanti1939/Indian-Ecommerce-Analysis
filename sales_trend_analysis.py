import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_dataset.csv")

df['visit_date'] = pd.to_datetime(df['visit_date'], dayfirst=True)

df['Year'] = df['visit_date'].dt.year
df['Month'] = df['visit_date'].dt.month
df['Month_Name'] = df['visit_date'].dt.strftime('%B')

monthly_sales = df.groupby(['Year', 'Month', 'Month_Name'])['revenue'].sum().reset_index()

yearly_sales = df.groupby('Year')['revenue'].sum().reset_index()

print("\n========== MONTHLY SALES ==========\n")
print(monthly_sales)

print("\n========== YEARLY SALES ==========\n")
print(yearly_sales)

peak_month = monthly_sales.loc[monthly_sales['revenue'].idxmax()]

low_month = monthly_sales.loc[monthly_sales['revenue'].idxmin()]

print("\n========== PEAK SALES MONTH ==========\n")
print(peak_month)

print("\n========== LOW SALES MONTH ==========\n")
print(low_month)

plt.figure(figsize=(12,6))

for year in monthly_sales['Year'].unique():
    data = monthly_sales[monthly_sales['Year'] == year]
    plt.plot(data['Month_Name'], data['revenue'], marker='o', label=str(year))

plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()

plt.savefig("monthly_sales_trend.png")

plt.show()

plt.figure(figsize=(8,5))

plt.bar(yearly_sales['Year'].astype(str), yearly_sales['revenue'])

plt.title("Yearly Sales Performance")
plt.xlabel("Year")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("yearly_sales_trend.png")

plt.show()

print("\n✅ Monthly and Yearly Sales Trend Analysis Completed")
print("✅ Charts saved successfully")

plt.figure(figsize=(12,6))

plt.bar(monthly_sales['Month_Name'], monthly_sales['revenue'])

plt.title("Monthly Sales Bar Chart")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("monthly_sales_bar_chart.png")

plt.show()

plt.figure(figsize=(8,5))

plt.bar(yearly_sales['Year'].astype(str), yearly_sales['revenue'])

plt.title("Yearly Sales Bar Chart")
plt.xlabel("Year")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("yearly_sales_bar_chart.png")

plt.show()

print("\n✅ Bar Charts Created Successfully")