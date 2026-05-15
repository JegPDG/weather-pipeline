import matplotlib.pyplot as plt
import pandas as pd

# CSV path for the Daily Summary 
csv_path_daily_summary = 'csv_files/daily_summary.csv'
csv_path_hourly_summary = 'csv_files/hourly_summary.csv'

# DAILY TREND  ----------------------------------------------------------------------------------

# Reading THe CSV file for Daily Summary 
dly_df = pd.read_csv(csv_path_daily_summary)

# Plotting the daily summary 
dly_df['day'] = pd.to_datetime(dly_df['day'])

dly_x = dly_df['day'].dt.strftime('%b %d')
dly_y = dly_df['avg_temp'].round(2)

# Bigger figure
plt.figure(figsize=(10, 7))

# Plotting the table 
plt.plot(dly_x, dly_y, marker = 'o')


# Graph labels 
plt.suptitle('Average Temperature in Aklan', fontsize=16, fontweight='bold')
plt.title('Over the course of the last 7 days', fontsize=12)
plt.xlabel('Days', fontweight='bold')
plt.ylabel('Average Temperature in °C', fontweight='bold')

# Label for each plot 
for i, v in enumerate(dly_y):
    plt.text(dly_x[i], v + 0.05, f"{v:.2f}°C", ha='center')

plt.savefig('charts/daily_trend.png')

plt.close()

# MIN AND MAXIMUM TEMPERATURE PER DAY ---------------------------------------------------------------------------------
# Data for X axis
dly_day_x = dly_x

# Data 1 for y axis
dly_max_1 = dly_df['max_temp']

# Data 2 for y axis
dly_min_1 = dly_df['min_temp']

# Bigger figure
plt.figure(figsize=(10, 7))

plt.plot(dly_day_x, dly_max_1, label='Maximum Temperature', marker='o')
plt.plot(dly_day_x, dly_min_1, label='Minimum Temperature',  marker='o')

plt.xlabel('Days', fontsize=14, fontweight='bold')
plt.ylabel('Temperature in °C', fontsize=14, fontweight='bold')
plt.suptitle('Minimum and maximum Temperature', fontsize=16, fontweight='bold')
plt.title('Temeperature range per day in the last & Days in Aklan')
plt.legend() # Displays labels defined in plt.plot()

plt.savefig('charts/min_max_trend.png')

plt.show()




#  NEXT TREND HOURLY AVERAGE TEMPERATURE ---------------------------------------------------------------------------------

# Reading the the hourly summary csv 
hly_df = pd.read_csv(csv_path_hourly_summary)

hly_x = hly_df['hour']
hly_y = hly_df['avg_temp']

# Bigger figure
plt.figure(figsize=(10, 7))

plt.bar(hly_x, hly_y)

# Labels 
month = pd.Timestamp.now(tz='Asia/Manila').month_name()

plt.suptitle('Hourly Average Temperature in Aklan', fontweight='bold', fontsize=16)
plt.title(f"In the month of {month}")
plt.xlabel("Hour", fontweight='bold')
plt.ylabel('Temperature in °C', fontweight='bold')

# for i, v in enumerate(hly_y):
#     plt.text(hly_x[i], v + 0.05, f"{v:.2f}")

plt.savefig('charts/hourly_trend.png')

# plt.close()









# print(hly_df.info())
# print(dly_df.info())


