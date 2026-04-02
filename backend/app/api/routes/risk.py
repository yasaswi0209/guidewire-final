from fastapi import APIRouter

from app.utils.weather_api import get_weather, get_aqi
from app.services.prediction_service import (
    calculate_risk,
    classify_risk,
    get_recommendation
)

router = APIRouter()


@router.get("/")
def get_risk(city: str = "Hyderabad"):   # ✅ dynamic input

    weather = get_weather(city)
    aqi = get_aqi(city)

    score = calculate_risk(weather, aqi)
    risk = classify_risk(score)

    recommendation = get_recommendation(risk)

    return {
        "city": city,
        "risk": risk,
        "score": score,
        "weather": weather,
        "aqi": aqi,
        "recommendation": recommendation
    }