import pandas as pd

# CSV file path
csv_path_clean = 'csv_files/api_data_clean.csv' 

# Load the data
df = pd.read_csv(csv_path_clean)

# Convert str date times into a Date Time data type
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["extracted_at"] = pd.to_datetime(df["extracted_at"])

# Create a new column for day and hour
df['hour'] = df['timestamp'].dt.floor('h')
df['day'] = df['timestamp'].dt.floor('D')

# Group by day
group_by_day = df.groupby('day').mean(numeric_only=True)

print(f"""
  Table 1: Group by day with an average temperature per day
  {group_by_day}""")

print(df.info())
print(df.head())

