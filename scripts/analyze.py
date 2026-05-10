import pandas as pd
from datetime import timedelta

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


# ///////////////////     GROUPED BY DAY      ///////////////

# Group by day
group_by_day = df.groupby('day').agg(
  avg_temp=('temperature_c', 'mean'),
  min_temp=('temperature_c', 'min'),
  max_temp=('temperature_c', 'max')
).sort_index(ascending=False)


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

print(recent_7_days)

# average_temp = recent_7_days['temperature_c'].mean()
# hottest_day = recent_7_days['temperature_c'].idxmax()
# hottest_temp = recent_7_days['temperature_c'].max().round(2)
# coldest_day = recent_7_days['temperature_c'].idxmin()
# coldest_temp = recent_7_days['temperature_c'].min().round(2)

# # //////////////////////// GROUPED BY HOUR ///////////////////////

# # Group by hour 
df['hour'] = df['hour'].dt.hour

group_by_hour = df.groupby('hour').agg(
  avg_temp=('temperature_c', 'mean'),
  min_temp=('temperature_c', 'min'),
  max_temp=('temperature_c', 'max'),

).round(2)

print(group_by_hour)

# # Hottest hour of the day 
# hottest_temp_by_hour = group_by_hour['temperature_c'].max().round(2)
# hottest_hour = group_by_hour['temperature_c'].idxmax()
# coldest_temp_by_hour = group_by_hour['temperature_c'].min().round(2)
# coldest_hour = group_by_hour['temperature_c'].idxmin()


# print(f"""
#   Table 1: The average temperature per day in Aklan
#   {avg_temp_per_day}

#   Average temperature in the last 7 days: {average_temp}
#   Hottest day in the last 7 days: {hottest_day} with a temperature of {hottest_temp}
#   Coldest day in the last 7 days: {coldest_day} with a temperature of {coldest_temp}

#   """)

# print(f""" 
#   Table 2: Group by hour
  

#   Hottest hour of the day: {hottest_temp_by_hour} at hour {hottest_hour}:00
#   Coldest hour of the day: {coldest_temp_by_hour} at hour {coldest_hour}:00

# """)


