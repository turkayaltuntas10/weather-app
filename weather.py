import requests
city = input("Please enter a city")
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
geo_response = requests.get(geo_url)
geo_data = geo_response.json()
latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
response = requests.get(url)
data = response.json()
temperature = data["current_weather"]["temperature"]
wind_speed = data["current_weather"]["windspeed"]
weather_code = data["current_weather"]["weathercode"]
print("Temperature :", temperature, "°C")
print("Wind speed :", wind_speed, "km/h")
print("Weather code :", weather_code)
