from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.db.session import get_db
from app.models.user import User
from app.core.security import verify_password, create_access_token, hash_password

router = APIRouter()

# ✅ SIMPLE USER SCHEMA
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    platform: str
    location: str
    weekly_income: float

# 🔐 SIGNUP (SIMPLIFIED)
@router.post("/signup")
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        platform=user.platform,
        location=user.location,
        weekly_income=user.weekly_income
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
    name=data.name,
    email=data.email,
    password=hash_password(data.password),
    platform=data.platform,
    location=data.location,
    weekly_income=data.weekly_income
)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}


# 🔐 LOGIN (same as before)
@router.post("/login")
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == form_data.username).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer",
        "name": db_user.name   # ✅ THIS LINE IS IMPORTANT
    }