import pandas as pd

# CSV file path
csv_path_clean = 'csv_files/api_data_clean.csv' 

# Load the data
df = pd.read_csv(csv_path_clean)

# Convert str date times into a Date Time data type
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["extracted_at"] = pd.to_datetime(df["extracted_at"])

# Create a new clumn for day and hour
df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.date




print(df)
print(df.info())

