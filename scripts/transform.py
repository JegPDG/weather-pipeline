import pandas as pd
import os

csv_path = 'csv_files/api_data_1.csv'
csv_path_new = 'csv_files/api_data_clean.csv'

df = pd.read_csv(csv_path)

# Convert str date times into a Date Time data type

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["extracted_at"] = pd.to_datetime(df["extracted_at"])

# Remove duplicates
df = df.drop_duplicates()


print(df.head())
print(df.info())
print(df.describe())

# Save transformations
df.to_csv(csv_path_new, mode='a', index=False, header=not os.path.exists(csv_path_new))

