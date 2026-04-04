from pydantic import BaseModel

class InsuranceCreate(BaseModel):
    plan_name: str
    coverage: int
    premium: int   # ✅ ADD THIS LINE