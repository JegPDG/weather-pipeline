import requests
from datetime import datetime
import pandas
import os

# Weather api URL
url = 'https://api.open-meteo.com/v1/forecast'
params = {
	"latitude": 16.5569,
	"longitude": 121.4774,
	"hourly": "temperature_2m",
	"current": "temperature_2m",
	"past_days": 0,
	"forecast_days": 7,
}

response = requests.get(url, params=params)

# CSV File path
csv_path = 'csv_files/api_data_1.csv' 

if response.status_code == 200:
  
	data = response.json()
	data["extracted_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
	timestamps = data['hourly']['time']
	temperatures = data["hourly"]["temperature_2m"]
  
	# Convert list of ditionaries into a DataFrame
	df = pandas.DataFrame({
    "extracted_at" : data["extracted_at"],
    "timestamp" : timestamps,
    "latitide" : data["latitude"],
    "longitude" : data["longitude"],
    "timezone": data["timezone"],
    "elevation": data["elevation"],
     "temperature_c": temperatures
	})
  
	# Append to CSV 
	df.to_csv(csv_path, mode='a', index=False, header=not os.path.exists(csv_path))
  

	print(df)
	print("File Saved")

  

else:
  print(f"Failed to retrieve data from Status code: {response.status_code }")