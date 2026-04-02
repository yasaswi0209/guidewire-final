import requests

WEATHER_API_KEY = "f894df03934102dedb72067d396c866e"
AQI_API_KEY = "61420ef3d4e1f4a8da8088c6fba76188f3303120"


def get_weather(city="Hyderabad"):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    res = requests.get(url).json()

    # 🔥 SAFE HANDLING
    if "main" not in res:
        print("Weather API Error:", res)
        return {"rain": 0, "temp": 30}

    rain = 0
    if "rain" in res:
        rain = res["rain"].get("1h", 0)

    temp = res["main"]["temp"]

    return {
        "rain": rain,
        "temp": temp
    }

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    res = requests.get(url).json()

    rain = 0
    if "rain" in res:
        rain = res["rain"].get("1h", 0)

    temp = res["main"]["temp"]

    return {
        "rain": rain,
        "temp": temp
    }


def get_aqi(city="hyderabad"):

    url = f"https://api.waqi.info/feed/{city}/?token={AQI_API_KEY}"

    res = requests.get(url).json()

    if res["status"] == "ok":
        return res["data"]["aqi"]

    return 100  # fallback