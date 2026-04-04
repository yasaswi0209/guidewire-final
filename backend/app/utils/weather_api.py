import requests

WEATHER_API_KEY = "f894df03934102dedb72067d396c866e"
AQI_API_KEY = "61420ef3d4e1f4a8da8088c6fba76188f3303120"

def get_weather_data(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()

    if "main" not in res:
        return {
            "rain": 0,
            "temp": 30,
            "humidity": 50
        }

    # 🌧️ Rain comes in mm → convert to 0/1
    rain_mm = res.get("rain", {}).get("1h", 0)
    rain = 1 if rain_mm > 0 else 0

    temp = res["main"]["temp"]
    humidity = res["main"]["humidity"]

    return {
        "rain": rain,
        "temp": temp,
        "humidity": humidity
    }


def get_aqi_data(city: str):
    url = f"https://api.waqi.info/feed/{city}/?token={AQI_API_KEY}"
    res = requests.get(url).json()

    if res.get("status") == "ok":
        return res["data"].get("aqi", 100)

    return 100
def get_weather_forecast(city: str):
    import requests

    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=YOUR_KEY&units=metric"
        res = requests.get(url).json()

        if "list" not in res:
            return {
                "temp": 30,
                "humidity": 50,
                "rain": 0
            }

        next_data = res["list"][1]

        temp = next_data["main"]["temp"]
        humidity = next_data["main"]["humidity"]
        rain = 1 if "rain" in next_data else 0

        return {
            "temp": temp,
            "humidity": humidity,
            "rain": rain
        }

    except Exception as e:
        print("Forecast API error:", e)

        # ✅ fallback (VERY IMPORTANT)
        return {
            "temp": 30,
            "humidity": 50,
            "rain": 0
        }