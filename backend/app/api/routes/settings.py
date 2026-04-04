from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.core.security import get_current_user 
router = APIRouter(prefix="/settings", tags=["Settings"])


# ✅ SAVE PAYMENT DETAILS
@router.post("/save")
def save_settings(
    data: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        user = db.query(User).filter(User.id == current_user.id).first()

        if not user:
            return {"error": "User not found"}

        user.phone = data.get("phone")
        user.upi = data.get("upi")
        user.bank_name = data.get("bank")

        db.commit()

        return {"message": "Saved successfully"}

    except Exception as e:
        print("ERROR:", e)
        return {"error": "Failed to save"}


# ✅ GET CURRENT USER PROFILE
@router.get("/profile/me")
def get_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == current_user.id).first()

    if not user:
        return {"error": "User not found"}

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "platform": user.platform,
        "location": user.location,
        "weekly_income": user.weekly_income,
        "phone": user.phone,
        "bank_name": user.bank_name,
        "upi_id": user.upi
    }


# ✅ UPDATE PROFILE
@router.put("/profile/update")
def update_profile(
    data: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        user = db.query(User).filter(User.id == current_user.id).first()

        if not user:
            return {"error": "User not found"}

        user.name = data.get("name", user.name)
        user.platform = data.get("platform", user.platform)
        user.location = data.get("location", user.location)
        user.weekly_income = data.get("weekly_income", user.weekly_income)
        user.phone = data.get("phone", user.phone)
        user.bank_name = data.get("bank_name", user.bank_name)
        user.upi = data.get("upi_id", user.upi)

        db.commit()

        return {"message": "Profile updated successfully"}

    except Exception as e:
        print("ERROR:", e)
        return {"error": "Update failed"}