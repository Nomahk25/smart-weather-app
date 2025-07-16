#weather_cli.py
from dotenv import load_dotenv
import os
from weather_api import fetch_weather

load_dotenv()
api_key = os.getenv("API_KEY")

def main():
    print("📍 Welcome to the Weather App (CLI)")
    city = input("🏙 Enter the city name: ")
    weather = fetch_weather(city, api_key)

    if not weather:
        print("❌ Failed to fetch weather data. Check your city name or API key.")
        return

    print(f"\n🌤 Weather in {weather['city']}:")
    print(f"🌡 Temperature: {weather['temperature']}°C")
    print(f"☁️ Condition: {weather['condition']}")
    print(f"💧 Humidity: {weather['humidity']}%")
    print(f"💨 Wind Speed: {weather['wind']} km/h")

if __name__ == "__main__":
    main()
