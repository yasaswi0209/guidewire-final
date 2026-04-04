import joblib
from app.utils.weather_api import get_weather_data, get_aqi_data

# 🔥 Load ML model
model = joblib.load("app/ml/premium_model.pkl")


def calculate_premium(city: str):

    # 🌦️ API DATA (SAFE FALLBACK)
    weather = get_weather_data(city) or {}
    aqi = get_aqi_data(city) or 100

    # 🔥 SAFE EXTRACTION
    temp = weather.get("temp", 30)
    humidity = weather.get("humidity", 50)
    rain = weather.get("rain", 0)

    # 🤖 ML prediction
    risk_score = model.predict([[aqi, temp, rain, humidity]])[0]

    trigger_prob = max(0.1, min(risk_score, 0.9))

    # 💰 Base income loss (TEMP BASED)
    if temp > 45:
        avg_income_loss = 700
    elif temp > 40:
        avg_income_loss = 600
    elif temp > 35:
        avg_income_loss = 500
    else:
        avg_income_loss = 400

    # 🌧️ Exposure
    days_exposed = 3 if rain > 0 else 1

    base_premium = (trigger_prob * avg_income_loss * days_exposed) / 100

    # 🌫️ AQI adjustment
    if aqi > 300:
        zone_factor = 1.5
        risk_level = "HIGH"
    elif aqi > 150:
        zone_factor = 1.2
        risk_level = "MEDIUM"
    else:
        zone_factor = 1.0
        risk_level = "LOW"

    # 🌧️ Rain adjustment
    if rain > 0:
        weather_factor = 1.3
        risk_level = "HIGH"
    else:
        weather_factor = 1.0

    # 🌡️ Temperature adjustment
    if temp > 45:
        temp_factor = 1.5
        risk_level = "HIGH"
    elif temp > 40:
        temp_factor = 1.3
        if risk_level != "HIGH":
            risk_level = "MEDIUM"
    elif temp > 35:
        temp_factor = 1.1
    else:
        temp_factor = 1.0

    # 👷 Worker factor
    worker_factor = 1.2

    # 🧮 Final premium
    final_premium = base_premium * zone_factor * weather_factor * worker_factor * temp_factor

    # 🎯 Clamp ₹20–₹50
    final_premium = max(20, min(final_premium, 50))

    return {
        "premium": round(final_premium, 2),
        "aqi": aqi,
        "temp": temp,
        "rain": rain,
        "humidity": humidity,
        "risk_score": float(risk_score),
        "risk_level": risk_level
    }