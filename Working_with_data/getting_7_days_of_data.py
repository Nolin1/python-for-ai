import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

today = datetime.now()
week_ago = today - timedelta(days=7)

#location
latitude = 48.85
longitude = 2.35

#formate the dates

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min")

data = response.json()

print(data["daily"])

# for i in range(len(data["daily"]["time"])):
#     print(f"{data["daily"]["time"][i]} : min {data["daily"]["temperature_2m_min"][i]}, max {data["daily"]["temperature_2m_max"][i]}")

daily_data = data["daily"]

#now create a dataframe
data_frame = pd.DataFrame({
    "Date" : daily_data["time"],
    "Max temp" : daily_data["temperature_2m_max"],
    "Min temp" : daily_data["temperature_2m_min"]
})

#converting the string into datetime
data_frame["Date"] = pd.to_datetime(data_frame["Date"])
data_frame["Max temp"] = pd.to_numeric(data_frame["Max temp"])

print(data_frame)

plt.figure(figsize=(10, 6))
plt.plot(data_frame['Date'], data_frame['Max temp'], marker='o', label='Max temp')
plt.plot(data_frame['Date'], data_frame['Min temp'], marker='o', label='Min temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

if not os.path.exists('data'):
    os.makedirs('data')

data_frame.to_csv('data/paris_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")