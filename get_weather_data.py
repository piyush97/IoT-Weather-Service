import json
import requests
import os
import time
from dotenv import load_dotenv

def get_env_vars():
    load_dotenv()
    envVar = {"APIKEY": "", "LAT": "", "LONG": ""}
    envVar["APIKEY"] = os.getenv("APP_ID")
    envVar["LAT"] = os.getenv("LAT")
    envVar["LONG"] = os.getenv("LONG")
    return envVar

def get_weather_data():
    envVar = get_env_vars()
    # use envVar to get the API key and location
    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + envVar["LAT"] + "&lon=" + envVar["LONG"] + "&appid=" + envVar["APIKEY"]
    response = requests.request("GET", url)
    data = json.loads(response.text)
    return data

def parse_weather_data():
    data = get_weather_data()
    temperature_celsius = data['main']['temp'] - 273.15  # Kelvin to Celsius conversion
    humidity = data['main']['humidity']
    raining = 'rain' in data
    wind_speed_kmh = data['wind']['speed'] * 3.6  # m/s to km/h conversion

    # Format the time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # Create the API response dictionary
    api_response = {
        "time": current_time,
        "temperature": round(temperature_celsius, 1),
        "humidity": humidity,
        "raining": raining,
        "windspeed": round(wind_speed_kmh, 1)
    }

    return api_response

