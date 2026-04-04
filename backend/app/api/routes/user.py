from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from app.core.security import create_access_token, hash_password
from app.db.session import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.api.deps import get_current_user

router = APIRouter()


# 👤 SIGNUP (AUTO LOGIN)
@router.post("/signup")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    # ✅ check if user exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # ✅ create user
    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        platform=user.platform,
        location=user.location,
        weekly_income=user.weekly_income
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # 🔥 AUTO LOGIN TOKEN
    access_token = create_access_token(
    {"sub": db_user.email},
    timedelta(hours=24)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# 🔍 GET USER BY ID
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# 🔐 GET CURRENT USER
@router.get("/me")
def get_profile(user=Depends(get_current_user)):
    return {"user": user}