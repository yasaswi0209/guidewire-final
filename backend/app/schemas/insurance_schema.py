from pydantic import BaseModel

class InsuranceCreate(BaseModel):
    plan_name: str
    premium: int
    coverage: int