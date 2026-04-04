from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.insurance import Insurance
from app.utils.weather_api import get_weather_data, get_aqi_data
from app.models.user import User
from app.ml.premium_model import calculate_premium
from app.models.user_bank import UserBank

def create_or_update_policy(db: Session, user_id: int, data):

    # 🧠 GET USER
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise Exception("User not found ❌")

    # 📍 LOCATION
    location = getattr(user, "location", "Hyderabad")

    # 🔍 CHECK EXISTING ACTIVE POLICY
    existing = db.query(Insurance).filter(
        Insurance.user_id == user_id,
        Insurance.status == "ACTIVE"
    ).first()

    # 🔒 LOCK CHECK (INSIDE FUNCTION ✅)
    if existing and existing.locked_until:
        if existing.locked_until > datetime.utcnow():
            return {
                "status": "locked",
                "message": f"Policy locked_until {existing.locked_until}"
            }

    # 🌦️ FETCH WEATHER + AQI
    try:
        weather = get_weather_data(location)
        aqi = get_aqi_data(location)
    except Exception as e:
        print("API ERROR:", e)
        weather = {"temp": 30, "rain": 0}
        aqi = 100

    # 🤖 ML PREMIUM
    premium_data = calculate_premium(location)
    premium = premium_data["premium"]

    print("📍 Location:", location)
    print("🌧️ Weather:", weather)
    print("🌫️ AQI:", aqi)
    print("💸 Premium:", premium)

    # ✅ UPDATE EXISTING POLICY
    if existing:
        existing.plan_name = data.plan_name
        existing.premium = premium
        existing.coverage = data.coverage
        existing.locked_until = datetime.utcnow() + timedelta(days=7)

        db.commit()
        db.refresh(existing)

        return {
            "status": "updated",
            "policy": existing
        }

    # ✅ CREATE NEW POLICY
    policy = Insurance(
        user_id=user_id,
        plan_name=data.plan_name,
        premium=premium,
        coverage=data.coverage,
        status="ACTIVE",
        locked_until=datetime.utcnow() + timedelta(days=7)
    )

    db.add(policy)
    db.commit()
    db.refresh(policy)

    return {
        "status": "created",
        "policy": policy
    }
# 🔥 GET ALL POLICIES
def get_user_policies(db: Session, user_id: int):
    return db.query(Insurance).filter(
        Insurance.user_id == user_id
    ).all()


# 🔥 GET LATEST POLICY
def get_latest_policy(db: Session, user_id: int):
    return db.query(Insurance).filter(
        Insurance.user_id == user_id
    ).order_by(Insurance.id.desc()).first()