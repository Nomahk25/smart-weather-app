import datetime
import requests

def fetch_weather(city, api_key):
    url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "status" in data:
        return None

    return {
        "city": data["city"],
        "temperature": data["temperature"]["current"],
        "humidity": data["temperature"]["humidity"],
        "condition": data["condition"]["description"],
        "wind": data["wind"]["speed"]
    }

def parse_date(value):
    if isinstance(value, int):
        return datetime.datetime.utcfromtimestamp(value).strftime("%Y-%m-%d")
    elif isinstance(value, str) and "T" in value:
        return value.split("T")[0]
    return str(value)  # fallback

def fetch_forecast(city, api_key):
    url = f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "daily" not in data or not data["daily"]:
        return []

    forecast_list = []
    for day in data["daily"][:3]:
        forecast_list.append({
            "day": parse_date(day["time"]),
            "temp": day["temperature"]["day"],
            "condition": day["condition"]["description"]
        })
    return forecast_list
