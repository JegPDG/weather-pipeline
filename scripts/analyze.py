import pandas as pd
from datetime import timedelta
import os

# CSV file path
csv_path_clean = 'csv_files/api_data_clean.csv' 
csv_path_daily_summary = 'csv_files/daily_summary.csv'
csv_path_hourly_summary = 'csv_files/hourly_summary.csv'


# Load the data
df = pd.read_csv(csv_path_clean)

# Convert str date times into a Date Time data type
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["extracted_at"] = pd.to_datetime(df["extracted_at"])

# Create a new column for day and hour
df['hour'] = df['timestamp'].dt.floor('h')
df['day'] = df['timestamp'].dt.floor('D')


# ///////////////////     GROUPED BY DAY      ///////////////

# Group by day
group_by_day = df.groupby('day').agg(
  avg_temp=('temperature_c', 'mean'),
  min_temp=('temperature_c', 'min'),
  max_temp=('temperature_c', 'max')
).sort_index(ascending=True)



# Getting today date
today = pd.Timestamp.today().normalize()

#  Group by day in the recently
recent_days = group_by_day[group_by_day.index <= today]

# Get the difference from the previous data 
recent_days['temp_diff_frm_day_before'] = recent_days['avg_temp'] - recent_days['avg_temp'].shift(-1)

# Last 7 days cutoff
last_7_days = today - timedelta(days=6)

# Filter only last 7 days and not future dates
recent_7_days = recent_days[
    (recent_days.index <= today) &
    (recent_days.index >= last_7_days)
]

recent_7_days['avg_temp_7_days'] = recent_7_days['avg_temp'].mean(numeric_only=True)

recent_7_days['temp_rise'] = recent_7_days['temp_diff_frm_day_before'].mean(numeric_only=True)

print(recent_7_days)

# Turn back index into a date 
recent_7_days = recent_7_days.reset_index()

recent_7_days.to_csv(csv_path_daily_summary, index=False)



# # //////////////////////// GROUPED BY HOUR ///////////////////////

# # Group by hour 
df['hour'] = df['hour'].dt.hour

group_by_hour = df.groupby('hour').agg(
  avg_temp=('temperature_c', 'mean'),
  min_temp=('temperature_c', 'min'),
  max_temp=('temperature_c', 'max'),

).round(2)

print(group_by_hour)

# Turn back index into a date 
group_by_hour = group_by_hour.reset_index()

group_by_hour.to_csv(csv_path_hourly_summary, index=False)




