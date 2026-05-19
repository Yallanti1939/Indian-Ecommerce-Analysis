import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_dataset.csv")

df['visit_date'] = pd.to_datetime(df['visit_date'])

df['Year'] = df['visit_date'].dt.year
df['Month'] = df['visit_date'].dt.month
df['Week'] = df['visit_date'].dt.isocalendar().week
df['Day'] = df['visit_date'].dt.day

daily_sales = df.groupby('visit_date')['revenue'].sum().reset_index()

daily_sales = daily_sales.sort_values('visit_date')

daily_sales.set_index('visit_date', inplace=True)

all_dates = pd.date_range(
    start=daily_sales.index.min(),
    end=daily_sales.index.max()
)

daily_sales = daily_sales.reindex(all_dates, fill_value=0)

daily_sales.index.name = 'Date'

print("\n========== DAILY SALES ==========\n")
print(daily_sales.head())

print("\n========== MISSING VALUES ==========\n")
print(daily_sales.isnull().sum())

trend = daily_sales['revenue'].rolling(window=7).mean()

plt.figure(figsize=(12,6))

plt.plot(
    daily_sales.index,
    daily_sales['revenue'],
    label='Daily Revenue'
)

plt.plot(
    daily_sales.index,
    trend,
    label='7-Day Trend'
)

plt.title("Daily Sales Trend Analysis")
plt.xlabel("Date")
plt.ylabel("Revenue")

plt.legend()

plt.tight_layout()

plt.savefig("daily_sales_trend.png")

plt.show()

monthly_sales = df.groupby(
    ['Year', 'Month']
)['revenue'].sum().reset_index()

plt.figure(figsize=(10,5))

plt.plot(
    monthly_sales['Month'],
    monthly_sales['revenue'],
    marker='o'
)

plt.title("Monthly Sales Seasonality")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("monthly_seasonality.png")

plt.show()

daily_sales.to_csv("time_series_dataset.csv")

print("\n✅ Time Series Dataset Prepared Successfully")
print("✅ Processed Dataset Saved")