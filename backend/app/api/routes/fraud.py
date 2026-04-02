from fastapi import APIRouter

router = APIRouter()

@router.get("/check/{user_id}")
def check_fraud(user_id: int):
    return {
        "user_id": user_id,
        "trust_score": 0.82,
        "status": "SAFE"
    }