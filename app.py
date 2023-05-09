from flask import Flask, render_template, request
import requests
import json, os
# from pprint import pprint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        city_name = request.form['city']
        api_key = os.getenv("weather_api_key")

        weather_url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric')

        weather_data = weather_url.json()
        # pprint(weather_data)

        temp = round(weather_data['main']['temp'])
        icon = weather_data["weather"][0]["icon"]
        weather = weather_data["weather"][0]["main"]
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        cloudiness = weather_data['clouds']['all']

        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, cloudiness=cloudiness, weather=weather, icon = icon, city=city_name)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
