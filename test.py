import requests
import json

city_name = "Nashik"

api_key = "WEATHER_API_KEY"

weather_url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric')

weather_data = weather_url.json()
print(weather_url.status_code)