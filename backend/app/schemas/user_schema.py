from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    platform: str     # ✅ ADD THIS
    location: str     # ✅ ADD THIS
    weekly_income: int

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True