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


# ///////////////////     GROUPED BY DAY ///////////////


# Group by day
group_by_day = df.groupby('day').mean(numeric_only=True).sort_index(ascending=False)

# Getting today date
today = pd.Timestamp.today().normalize()

# Group by day in the recently
avg_temp_per_day = group_by_day[group_by_day.index <= today]

# Get the difference from the previous data 
avg_temp_per_day['yesterday_temp'] = avg_temp_per_day['temperature_c'].shift(-1)

avg_temp_per_day['temp_difference'] = avg_temp_per_day['temperature_c'] - avg_temp_per_day['yesterday_temp']


# Last 7 days cutoff
last_7_days = today - timedelta(days=7)

# Filter only last 7 days and not future dates
recent_7_days = group_by_day[
    (group_by_day.index <= today) &
    (group_by_day.index >= last_7_days)
]

average_temp = recent_7_days['temperature_c'].mean()
hottest_day = recent_7_days['temperature_c'].idxmax()
hottest_temp = recent_7_days['temperature_c'].max()
coldest_day = recent_7_days['temperature_c'].idxmin()
coldest_temp = recent_7_days['temperature_c'].min()

# //////////////////////// GROUPED BY HOUR ///////////////////////

# Group by hour 
group_by_hour = df.groupby('hour').mean(numeric_only=True).sort_index(ascending=False)

# Last 7 days cutoff 
last_7_days_by_hour = group_by_hour[(group_by_hour.index <= today) & (group_by_hour.index >= last_7_days)]


print(f"""
  Table 1: The average temperature per day in Aklan
  {avg_temp_per_day}

  Q: Is it getting hotter or colder here in Aklan
    Data shows that the temparature difference from the day before is
    showing a positive value, which means that the temperature the next day is getting higher.
    The data shows that the temperature is getting hotter day by day.

  Average temperature in the last 7 days: {average_temp}
  Hottest day in the last 7 days: {hottest_day} with a temperature of {hottest_temp}
  Coldest day in the last 7 days: {coldest_day} with a temperature of {coldest_temp}

  """)

print(f""" 
  Table 2: Group by Hour in the
  {last_7_days_by_hour}

""")


