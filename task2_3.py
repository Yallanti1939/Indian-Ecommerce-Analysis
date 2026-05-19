import pandas as pd

df = pd.read_csv("Ecommerce.csv")

print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())

print("\n========== DATASET INFO ==========\n")
print(df.info())

print("\n========== DATASET SHAPE ==========\n")
print(df.shape)

print("\n========== COLUMN NAMES ==========\n")
print(df.columns)

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

print("\n========== STATISTICAL SUMMARY ==========\n")
print(df.describe())

print("\n========== CLEANING PROCESS ==========\n")

df.drop_duplicates(inplace=True)

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

object_cols = df.select_dtypes(include=['object', 'string']).columns

for col in object_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

if 'visit_date' in df.columns:
    df['visit_date'] = pd.to_datetime(
        df['visit_date'],
        dayfirst=True,
        errors='coerce'
    )

print("\n========== MISSING VALUES AFTER CLEANING ==========\n")
print(df.isnull().sum())

df.to_csv("cleaned_dataset.csv", index=False)

print("\n✅ Data Cleaning Completed Successfully")
print("✅ Cleaned file saved as cleaned_dataset.csv")