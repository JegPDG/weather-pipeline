import matplotlib.pyplot as plt
import pandas as pd

# CSV path for the Daily Summary 
csv_path_daily_summary = 'csv_files/daily_summary.csv'

# Reading THe CSV file for Daily Summary 
dly_df = pd.read_csv(csv_path_daily_summary)

# Plotting the daily summary 
dly_df['day'] = pd.to_datetime(dly_df['day'])

dly_x = dly_df['day'].dt.strftime('%b %d')
dly_y = dly_df['avg_temp']

# Bigger figure
plt.figure(figsize=(10, 5))

# Plotting the table 
plt.plot(dly_x, dly_y, marker = 'o')


# Graph labels 
plt.title('Daily Summary')
plt.xlabel('Days')
plt.ylabel('Average Temperature')

# Show Plotting 
plt.show()

print(dly_df.info())