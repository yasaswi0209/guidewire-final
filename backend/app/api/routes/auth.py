from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import timedelta

from app.db.session import get_db
from app.models.user import User
from app.core.security import verify_password, create_access_token, hash_password

router = APIRouter()

# ✅ USER SCHEMA
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    platform: str
    location: str
    weekly_income: float


# 🔐 SIGNUP
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")

        new_user = User(
            name=user.name,
            email=user.email,
            password=hash_password(user.password),
            platform=user.platform,
            location=user.location,
            weekly_income=int(user.weekly_income)  # 🔥 FIX
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        access_token = create_access_token(
            {"sub": new_user.email},
            timedelta(hours=24)
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    except Exception as e:
        print("🔥 SIGNUP ERROR:", str(e))
        raise HTTPException(status_code=500, detail="Signup failed")

# 🔐 LOGIN
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == form_data.username).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        {"sub": db_user.email},
        timedelta(hours=24)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }