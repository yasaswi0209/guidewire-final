from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.user import User
from app.services.payout_service import check_and_trigger_payout
from app.services.prediction_service import calculate_premium

router = APIRouter()


# ✅ DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🚀 PAYOUT API
@router.get("/payout/{user_id}")
def payout(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"error": "User not found"}

    location = user.location  # ✅ correct field

    return check_and_trigger_payout(location)


# 💰 PREMIUM API
@router.get("/premium/{user_id}")
def premium(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"error": "User not found"}

    location = user.location

    return calculate_premium(location)