import os
import joblib
from app.utils.weather_api import get_weather_data, get_aqi_data

# 🔥 Safe path (IMPORTANT)
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "premium_model.pkl")

model = joblib.load(model_path)
try:
    model = joblib.load(model_path)
except Exception as e:
    print("MODEL LOAD ERROR:", e)
    model = None


def calculate_premium(city: str):

    # 🌦️ Fetch data
    weather = get_weather_data(city) or {}
    aqi = get_aqi_data(city) or 100

    temp = weather.get("temp", 30)
    humidity = weather.get("humidity", 50)
    rain = weather.get("rain", 0)

    # 🤖 ML prediction
    if model is None:
        risk_score = 0.5  # safe default
    else:
        risk_score = float(model.predict([[aqi, temp, rain, humidity]])[0])

    # 🔥 Convert to safe probability
    trigger_prob = max(0.1, min(risk_score, 0.9))

    # ====================================================
    # 🔥 SMART RISK SCORING
    # ====================================================
    score = 0

    if temp > 40:
        score += 2
    elif temp > 35:
        score += 1

    if rain > 0:
        score += 2

    if aqi > 200:
        score += 3
    elif aqi > 100:
        score += 2

    if score >= 4:
        risk_level = "HIGH"
    elif score >= 2:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    # ====================================================
    # 💰 BASE INCOME LOSS
    # ====================================================
    if temp > 45:
        avg_income_loss = 700
    elif temp > 40:
        avg_income_loss = 600
    elif temp > 35:
        avg_income_loss = 500
    else:
        avg_income_loss = 400

    days_exposed = 3 if rain > 0 else 1

    # ====================================================
    # 🔥 STEP 1: BASE PREMIUM
    # ====================================================
    base_premium = (trigger_prob * avg_income_loss * days_exposed) / 10

    # ====================================================
    # 🔥 STEP 2: NORMALIZE (0–1)
    # ====================================================
    normalized = min(max(base_premium / 100, 0), 1)

    # ====================================================
    # 🎯 RANGE BASED ON RISK
    # ====================================================
    if risk_level == "LOW":
        min_p, max_p = 20, 30
    elif risk_level == "MEDIUM":
        min_p, max_p = 30, 42
    else:
        min_p, max_p = 42, 52

    # ====================================================
    # 🔥 STEP 3: MAP INSIDE RANGE
    # ====================================================
    final_premium = min_p + (normalized * (max_p - min_p))

    # ====================================================
    # 🔒 FINAL SAFETY
    # ====================================================
    final_premium = max(20, min(final_premium, 52))

    return {
        "premium": round(final_premium, 2),
        "aqi": aqi,
        "temp": temp,
        "rain": rain,
        "humidity": humidity,
        "risk_score": risk_score,
        "risk_level": risk_level
    }