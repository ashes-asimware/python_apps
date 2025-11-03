'''
The following module includes process for connecting to APIs using external tools.
'''
import requests

lati = 40.7128
longi = -74.0060

weather_api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lati}&longitude={longi}&current_weather=true"

response = requests.get(weather_api_url)

if response.status_code == 200:
    weather_data = response.json()
    current_weather = weather_data.get("current_weather", {})
    temperature = current_weather.get("temperature")
    windspeed = current_weather.get("windspeed")
    print(f"Current Temperature: {temperature}°C")
    print(f"Current Windspeed: {windspeed} km/h")
else:
    print("Failed to retrieve weather data")






