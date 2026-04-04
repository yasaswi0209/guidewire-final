from fastapi import APIRouter

router = APIRouter()

# ✅ SAFE ROUTE (NO DB)
@router.get("/insurance/me")
def get_user_policy():
    return {
        "plan": "Basic",
        "status": "active",
        "weekly_premium": 23.6
    }

# ✅ MATCH FRONTEND (IMPORTANT → POST, not GET)
@router.post("/insurance/upgrade")
def upgrade_plan(plan: str):
    return {
        "message": f"{plan} plan activated 🎉"
    }