import requests

# We need coordinates to get weather data
latitude = 23.777   # Paris latitude
longitude = 90.399   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

type(data)

data.keys()

data["current"]

data["current"] ["temperature_2m"]


