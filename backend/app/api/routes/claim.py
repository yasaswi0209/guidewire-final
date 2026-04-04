from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.models.claim import Claim   # 👈 make sure import is there

from app.db.session import get_db
from app.services.claim_service import create_claim, auto_claim_logic
from app.utils.weather_api import get_weather_data, get_aqi_data

import random
from datetime import datetime   # ✅ REQUIRED

router = APIRouter(prefix="/claims", tags=["Claims"])


@router.post("/auto")
def auto_claim(request: dict = Body(...), db: Session = Depends(get_db)):

    try:
        # 👤 USER
        user_id = request.get("user_id") or 1
        city = request.get("city", "Hyderabad")
        trigger = request.get("trigger")

        # 🌍 WEATHER + AQI
        weather = get_weather_data(city) or {}
        aqi = get_aqi_data(city) or 100

        temp = weather.get("temp", 30)
        rain = weather.get("rain", 0)
        condition = weather.get("condition", "clear")

        # 🎯 CONTROLLED DEMAND BASED ON TRIGGER (MAIN FIX)
        if trigger == "rain":
            orders = random.randint(1, 4)
            rain = max(rain, 60)
        elif trigger == "heat":
            orders = random.randint(2, 5)
            temp = max(temp, 42)
        elif trigger == "pollution":
            orders = random.randint(1, 3)
            aqi = max(aqi, 180)
        elif trigger == "curfew":
            orders = 0
            aqi = max(aqi, 320)
        else:
            orders = random.randint(8, 15)

        # 🚫 CURFEW LOGIC
        is_curfew = (temp > 45 or aqi > 300)

        # 🧠 WEATHER FORMAT
        weather_data = {
            "type": "rain" if rain > 0 else condition,
            "temp": temp,
            "rain": rain
        }

        # 🤖 CLAIM LOGIC
        amount, reason, risk_score = auto_claim_logic(
            weather_data, aqi, orders, is_curfew
        )

        # ❌ NO CLAIM
        if amount <= 0:
            return {
                "message": "No claim triggered",
                "claim_id": None,
                "city": city,
                "amount": 0,
                "reason": reason,
                "risk_score": risk_score,
                "status": "rejected",
                "fraud": False,
                "fraud_reason": "Low risk / No trigger",
                "payment_status": "failed",
                "payment": None,
                "weather": {
                    "temp": temp,
                    "rain": rain,
                    "condition": condition
                },
                "aqi": aqi,
                "orders": orders
            }

        # 💾 CREATE CLAIM
        claim, fraud_reason, payment_data = create_claim(
            db=db,
            user_id=user_id,
            trigger=reason,
            risk_score=risk_score,
            amount=amount
        )

        # 💸 PAYMENT STATUS
        payment_status = "success" if claim and claim.status == "approved" else "failed"

        # ✅ ADD TIME (CORRECT PLACE)
        if payment_data:
            payment_data["time"] = datetime.now().strftime("%d %b %Y, %I:%M %p")

        # 📤 RESPONSE
        return {
            "message": "🔥 Fully Automated AI Claim",
            "claim_id": claim.id,
            "city": city,
            "amount": claim.amount,
            "reason": reason,
            "risk_score": risk_score,
            "status": claim.status,
            "fraud": claim.is_fraud,
            "fraud_reason": fraud_reason,
            "payment_status": payment_status,
            "payment": payment_data,
            "weather": {
                "temp": temp,
                "rain": rain,
                "condition": condition
            },
            "aqi": aqi,
            "orders": orders,
            "trigger": trigger
        }

    except Exception as e:
        print("❌ ERROR:", str(e))

        return {
            "message": "Server error",
            "error": str(e),
            "status": "failed",
            "payment": None
        }


@router.get("/recent")
def get_recent_claims(db: Session = Depends(get_db)):
    claims = db.query(Claim).order_by(Claim.id.desc()).limit(5).all()

    return [
        {
            "type": c.trigger_type,
            "amount": c.amount,
            "date": c.created_at.strftime("%d %b")
        }
        for c in claims
    ]


@router.get("/weather/{city}")
def get_weather(city: str):
    from app.utils.weather_api import get_weather_data, get_aqi_data

    weather = get_weather_data(city) or {}
    aqi = get_aqi_data(city) or 100

    return {
        "temp": weather.get("temp", 30),
        "rain": weather.get("rain", 0),
        "condition": weather.get("condition", "clear"),
        "aqi": aqi
    }


@router.post("/risk")
def calculate_risk(data: dict):

    weather = data.get("weather")
    aqi = data.get("aqi")

    if not weather or aqi is None:
        return {"error": "Missing input"}

    level = ""
    reason = ""

    if weather == "rain" and aqi > 150:
        level = "High"
        reason = "Rain + poor air quality"

    elif weather == "rain":
        level = "Medium"
        reason = "Rain disruption possible"

    elif weather == "heat":
        level = "Medium"
        reason = "Extreme heat fatigue"

    elif aqi > 150:
        level = "High"
        reason = "Severe pollution"

    else:
        level = "Low"
        reason = "Normal environment"

    return {
        "risk": level,
        "reason": reason
    }