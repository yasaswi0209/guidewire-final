from pydantic import BaseModel

class UserSignup(BaseModel):
    name: str
    email: str
    password: str
    zone: str
    weekly_income: float

class UserLogin(BaseModel):
    email: str
    password: str   