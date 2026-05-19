import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error
import numpy as np

df = pd.read_csv("time_series_dataset.csv")

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

train_size = int(len(df) * 0.8)

train = df.iloc[:train_size]
test = df.iloc[train_size:]

model = ExponentialSmoothing(
    train['revenue'],
    trend='add',
    seasonal=None
)

fit_model = model.fit()

forecast = fit_model.forecast(len(test))

rmse = np.sqrt(
    mean_squared_error(
        test['revenue'],
        forecast
    )
)

print("\n========== RMSE ==========\n")
print(rmse)

future_forecast = fit_model.forecast(365)

print("\n========== FUTURE SALES FORECAST ==========\n")
print(future_forecast)

plt.figure(figsize=(12,6))

plt.plot(
    train.index,
    train['revenue'],
    label='Training Data'
)

plt.plot(
    test.index,
    test['revenue'],
    label='Actual Sales'
)

plt.plot(
    test.index,
    forecast,
    label='Forecasted Sales'
)

plt.title("Sales Forecasting")

plt.xlabel("Date")
plt.ylabel("Revenue")

plt.legend()

plt.tight_layout()

plt.savefig("sales_forecast_chart.png")

plt.show()

plt.figure(figsize=(12,6))

plt.plot(
    future_forecast.index,
    future_forecast.values
)

plt.title("Future Sales Forecast")

plt.xlabel("Future Dates")
plt.ylabel("Predicted Revenue")

plt.tight_layout()

plt.savefig("future_sales_forecast.png")

plt.show()

future_forecast.to_csv("future_sales_predictions.csv")

print("\n✅ Forecasting Model Applied Successfully")
print("✅ Future Sales Predictions Generated")