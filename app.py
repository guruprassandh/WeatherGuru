
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Your WeatherAPI key
WEATHER_API_KEY = "a09b7f58e3994b78add160541242311"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    if not city:
        return "City not found!", 400

    # Send a request to WeatherAPI
    params = {
        "key": WEATHER_API_KEY,
        "q": city,
        "aqi": "no"  # Exclude air quality index for simplicity
    }
    response = requests.get(WEATHER_API_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return render_template("index.html", weather=weather_data)
    else:
        error_message = response.json().get("error", {}).get("message", "Unknown error")
        return f"Error: {error_message}", 400

if __name__ == "__main__":
    app.run(debug=True)

