from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.api.deps import get_current_user
from app.ml.premium_model import calculate_premium  
from app.utils.weather_api import get_weather_data, get_aqi_data
from app.ml.premium_model import calculate_premium

router = APIRouter()

# 🔥 DEMO CONTROL
DEMO_MODE = False
DEMO_SCENARIO = "HIGH"   # LOW / MEDIUM / HIGH


@router.get("/")
def get_risk(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # 🔐 Fetch user
    db_user = db.query(User).filter(User.id == current_user.id).first()

    if not db_user:
        raise Exception("User not found")

    # 📍 City from DB (fallback safe)
    city = "Hyderabad" if DEMO_MODE else getattr(db_user, "location", "Hyderabad")

    # 🌦️ Fetch real data
    weather = get_weather_data(city) or {"temp": 30, "rain": 0}
    aqi = get_aqi_data(city) or 100

    # 🔥 DEMO OVERRIDE (for testing UI)
    if DEMO_MODE:
        if DEMO_SCENARIO == "LOW":
            weather["temp"] = 28
            weather["rain"] = 0
            aqi = 80

        elif DEMO_SCENARIO == "MEDIUM":
            weather["temp"] = 36
            weather["rain"] = 0
            aqi = 150

        elif DEMO_SCENARIO == "HIGH":
            weather["temp"] = 42
            weather["rain"] = 1
            aqi = 250

    temp = weather.get("temp", 30)
    rain = weather.get("rain", 0)

    explanation = []

    # 🔥 Explain logic (for UI)
    if temp > 40:
        explanation.append("Extreme heat (>40°C) increases fatigue risk")
    elif temp > 35:
        explanation.append("High temperature affects worker performance")
    else:
        explanation.append("Temperature is within safe range")

    if rain > 0:
        explanation.append("Rain may cause delays and accident risk")
    else:
        explanation.append("No rainfall disruption expected")

    if aqi > 200:
        explanation.append("Severe pollution impacts health")
    elif aqi > 100:
        explanation.append("Moderate pollution detected")
    else:
        explanation.append("Air quality is safe")

    # 🤖 ML CORE
    premium_data = calculate_premium(city)

    ml_price = premium_data["premium"]
    risk = premium_data["risk_level"]

    # 🎯 Recommendation + badge logic
    if risk == "HIGH":
        recommendation = "Premium Plan Recommended"
        explanation.append("High risk → higher premium 🔴")

    elif risk == "MEDIUM":
        recommendation = "Moderate Plan Recommended"
        explanation.append("Moderate risk → balanced pricing 🟡")

    else:
        recommendation = "Basic Plan Recommended"
        explanation.append("Low risk → lower premium 🟢")

    reason = " | ".join(explanation)

    return {
        "city": city,
        "risk": risk,
        "weather": weather,
        "aqi": aqi,
        "ml_price": ml_price,
        "reason": reason,
        "recommendation": recommendation
    }