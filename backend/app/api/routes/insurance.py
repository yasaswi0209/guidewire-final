from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.insurance import Insurance
from app.schemas.insurance_schema import InsuranceCreate
from app.api.deps import get_current_user

router = APIRouter()


# 🔥 CREATE / UPDATE POLICY
@router.post("/")
def create_policy(
    data: InsuranceCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    try:

        existing = db.query(Insurance).filter(
            Insurance.user_id == user.id,
            Insurance.status == "ACTIVE"
        ).first()

        # ✅ UPDATE IF EXISTS
        if existing:
            existing.plan_name = data.plan_name
            existing.premium = data.premium
            existing.coverage = data.coverage

            db.commit()
            db.refresh(existing)

            return {
                "message": "Plan updated successfully 🔄",
                "policy": existing
            }

        # ✅ CREATE NEW
        policy = Insurance(
            user_id=user.id,
            plan_name=data.plan_name,
            premium=data.premium,
            coverage=data.coverage,
            status="ACTIVE"
        )

        db.add(policy)
        db.commit()
        db.refresh(policy)

        return {
            "message": "Policy created successfully ✅",
            "policy": policy
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Failed to create policy")


# 🔥 GET ALL USER POLICIES
@router.get("/plans")
def get_my_policies(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    try:
        return db.query(Insurance).filter(
            Insurance.user_id == user.id
        ).all()

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Failed to fetch policies")


# 🔥 GET LATEST POLICY (FOR DASHBOARD)
@router.get("/my")
def get_latest_policy(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    try:
        policy = db.query(Insurance).filter(
            Insurance.user_id == user.id
        ).order_by(Insurance.id.desc()).first()

        if not policy:
            return {
                "plan_name": None,
                "premium": 0
            }

        return {
            "plan_name": policy.plan_name,
            "premium": policy.premium
        }

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Failed to fetch policy")