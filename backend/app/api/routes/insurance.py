from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.db.session import get_db
from app.schemas.insurance_schema import InsuranceCreate
from app.api.deps import get_current_user
from app.services.insurance_service import (
    create_or_update_policy,
    get_user_policies,
    get_latest_policy
)
from app.models.insurance import Insurance

router = APIRouter(prefix="/insurance", tags=["Insurance"])


# 🔥 CREATE / UPDATE POLICY
@router.post("/")
def create_policy(
    data: InsuranceCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    try:
        policy, action = create_or_update_policy(db, user.id, data)

        return {
            "message": f"Policy {action} successfully ✅",
            "policy": policy
        }

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Failed to create/update policy")


# 🔥 GET ALL POLICIES
@router.get("/plans")
def get_my_policies(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    try:
        return get_user_policies(db, user.id)

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Failed to fetch policies")


# 🔥 DASHBOARD DATA
@router.get("/my")
def get_my_policy(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    try:
        policy = get_latest_policy(db, user.id)

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


# 🔒 GET LOCK STATUS
@router.get("/me")
def get_policy_lock_status(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    try:
        policy = get_latest_policy(db, user.id)

        if not policy:
            return {}

        print("FETCH LOCK:", policy.locked_until)  # DEBUG

        return {
            "plan": policy.plan_name,
            "locked_until": policy.locked_until.isoformat() if policy.locked_until else None
        }

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Failed to fetch lock status")


# 🚀 UPGRADE PLAN (FINAL VERSION)
@router.post("/upgrade")
def upgrade_plan(
    plan: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    try:

        premium_map = {
            "Basic": 20,
            "Moderate": 50,
            "Premium": 100
        }

        coverage_map = {
            "Basic": 5000,
            "Moderate": 10000,
            "Premium": 20000
        }

        premium = premium_map.get(plan)
        coverage = coverage_map.get(plan)

        if premium is None or coverage is None:
            raise HTTPException(status_code=400, detail="Invalid plan")

        policy = get_latest_policy(db, user.id)

        # 🔥 UPDATE OR CREATE
        if policy:
            policy.plan_name = plan
            policy.premium = premium
            policy.coverage = coverage
            action = "updated"
        else:
            policy = Insurance(
                user_id=user.id,
                plan_name=plan,
                premium=premium,
                coverage=coverage
            )
            db.add(policy)
            action = "created"

        # 🔒 LOCK FOR 7 DAYS (CORE FEATURE)
        policy.locked_until = datetime.utcnow() + timedelta(days=7)

        # ✅ SAVE
        db.commit()
        db.refresh(policy)

        print("LOCK SET:", policy.locked_until)  # DEBUG

        return {
            "message": f"Plan upgraded successfully 🚀 ({action})",
            "plan": policy.plan_name,
            "premium": policy.premium,
            "locked_until": policy.locked_until.isoformat()
        }

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Failed to upgrade plan")