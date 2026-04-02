from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/predict-risk")
def predict_risk(data: dict):

    aqi = data.get("aqi")
    weather = data.get("weather")

    # ✅ Validation
    if aqi is None:
        raise HTTPException(status_code=400, detail="AQI is required")

    try:
        aqi = float(aqi)
    except:
        raise HTTPException(status_code=400, detail="Invalid AQI value")

    if weather is None:
        weather = "normal"

    weather = weather.lower()

    print("AQI:", aqi, "| Weather:", weather)

    # ✅ Smart Logic (AQI + Weather)
    if aqi > 200:
        risk = "High"
        confidence = 95
        reason = "Severe pollution levels"
    elif aqi > 100 and weather == "rain":
        risk = "High"
        confidence = 90
        reason = "Rain + moderate pollution increases risk"
    elif aqi > 50:
        risk = "Medium"
        confidence = 75
        reason = "Moderate air quality"
    else:
        risk = "Low"
        confidence = 85
        reason = "Safe environment"

    return {
        "risk": risk,
        "confidence": confidence,
        "reason": reason
    }