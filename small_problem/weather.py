import requests

def check_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()
    return data["current"]["temperature_2m"]

paris = check_weather(48.85, 2.35)
bangladesh = check_weather(23.777, 90.399)
australia = check_weather(33.8688, 151.2093)

print(f"Paris: {paris}c")
print(f"Bangladesh: {bangladesh}c")
print(f"Australia: {australia}c")