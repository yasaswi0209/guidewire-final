from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.payout import Payout
from app.models.user import User
from app.models.community_pool import CommunityPool
from app.services.pool_service import deduct_from_pool

router = APIRouter()

@router.post("/{user_id}")
def process_payout(user_id: int, db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    payout_amount = 200  # dummy logic

    success = deduct_from_pool(db, user.zone, payout_amount)

    if not success:
        raise HTTPException(status_code=400, detail="Insufficient pool funds")

    payout = Payout(
        user_id=user.id,
        amount=payout_amount,
        reason="Rain disruption"
    )

    db.add(payout)
    db.commit()
    db.refresh(payout)

    return {"message": "Payout processed", "amount": payout_amount}