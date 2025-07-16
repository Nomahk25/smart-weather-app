#app.py
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from weather_api import fetch_weather, fetch_forecast

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])

# def weather():
#     #city = request.form.get("city")
#     data = request.get_json()
#     city = data.get("city")

#     print("🔍 Fetching weather for:", city)
    
#     if not city:
#         return jsonify({"error": "City is required"}), 400

#     current = fetch_weather(city, API_KEY)
#     forecast = fetch_forecast(city, API_KEY)

#     if not current or not forecast:
#         print("❌ Error fetching current or forecast data")
#         return jsonify({"error": "Failed to fetch weather data."}), 400

#     print("✅ Success:", current["city"])
#     current["forecast"] = forecast
#     return jsonify(current)

@app.route("/weather", methods=["POST"])
def weather():
    try:
        data = request.get_json()
        city = data.get("city")
        print("🔍 Fetching weather for:", city)
        
        if not city:
            return jsonify({"error": "City is required"}), 400

        current = fetch_weather(city, API_KEY)
        forecast = fetch_forecast(city, API_KEY)

        if not current or not forecast:
            print("❌ Error fetching current or forecast data")
            return jsonify({"error": "Failed to fetch weather data."}), 400

        print("✅ Success:", current["city"])
        current["forecast"] = forecast
        return jsonify(current)

    except Exception as e:
        print("🔥 Exception occurred:", e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
