from sqlalchemy.orm import Session
from app.models.claim import Claim
from app.services.fraud_service import check_fraud
from app.utils.payment_gateway import process_payout


# ============================================================
# 🧾 CREATE CLAIM (DB + FRAUD + PAYMENT)
# ============================================================
def create_claim(db: Session, user_id: int, trigger: str, risk_score: float, amount: int):

    # 🚨 Fraud check
    is_fraud, fraud_reason = check_fraud(user_id, amount, risk_score)
    status = "rejected" if is_fraud else "approved"

    # 💾 Save claim
    claim = Claim(
        user_id=user_id,
        trigger_type=trigger,
        risk_score=risk_score,
        amount=amount,
        status=status,
        is_fraud=is_fraud
    )

    db.add(claim)
    db.commit()
    db.refresh(claim)

    # 💸 PAYMENT (auto payout)
    payment_data = None

    if not is_fraud and amount > 0:
        payment_data = process_payout(user_id, amount)

    return claim, fraud_reason, payment_data


# ============================================================
# 🤖 AUTO CLAIM LOGIC (AI ENGINE)
# ============================================================
# ============================================================
# 🤖 AUTO CLAIM LOGIC (AI ENGINE)
# ============================================================
def auto_claim_logic(weather: dict, aqi: int, orders: int, is_curfew: bool = False):

    amount = 0
    reasons = []
    risk_score = 0

    rain = weather.get("rain", 0)
    temp = weather.get("temp", 0)

    # 🌧️ RAIN CONDITIONS
    if rain >= 20 and rain < 50:
        amount += 150
        risk_score += 0.2
        reasons.append("Moderate Rain 🌧️")

    elif rain >= 50 and rain < 80:
        amount += 250
        risk_score += 0.3
        reasons.append("Heavy Rain 🌧️")

    elif rain >= 80:
        amount += 350
        risk_score += 0.4
        reasons.append("Extreme Rain 🚨")

    # 🔥 HEAT CONDITIONS
    if temp >= 40 and temp < 45:
        amount += 150
        risk_score += 0.2
        reasons.append("Heatwave 🔥")

    elif temp >= 45:
        amount += 250
        risk_score += 0.3
        reasons.append("Extreme Heat 🚨")

    # 🌫️ AIR POLLUTION
    if aqi >= 150 and aqi < 300:
        amount += 150
        risk_score += 0.2
        reasons.append("High Pollution 🌫️")

    elif aqi >= 300:
        amount += 250
        risk_score += 0.3
        reasons.append("Severe Pollution 🚨")

    # 🚫 CURFEW (highest priority)
    if is_curfew:
        amount += 300
        risk_score += 0.4
        reasons.append("Government Curfew 🚫")

    # 📉 LOW DEMAND
    if orders < 5:
        amount += 50
        risk_score += 0.1
        reasons.append("Low Demand 📉")

    # 🔒 LIMIT VALUES
    risk_score = min(round(risk_score, 2), 1.0)
    amount = min(amount, 700)

    # 🎯 ENSURE MINIMUM IF TRIGGERED
    if amount > 0:
        amount = max(amount, 150)

    # ❌ NO TRIGGER CASE
    if amount == 0:
        return 0, "No threshold crossed", 0

    return amount, ", ".join(reasons), risk_score

    amount = 0
    reasons = []
    risk_score = 0

    rain = weather.get("rain", 0)
    temp = weather.get("temp", 0)

    # 🌧️ RAIN CONDITIONS
    if rain >= 20:
        amount += 200
        risk_score += 0.3
        reasons.append("Moderate Rain 🌧️")

    if rain >= 50:
        amount += 150
        risk_score += 0.2
        reasons.append("Heavy Rain 🌧️")

    if rain >= 80:
        amount += 200
        risk_score += 0.2
        reasons.append("Extreme Rain 🚨")

    # 🔥 HEAT CONDITIONS
    if temp >= 40:
        amount += 200
        risk_score += 0.3
        reasons.append("Heatwave 🔥")

    if temp >= 45:
        amount += 200
        risk_score += 0.2
        reasons.append("Extreme Heat 🚨")

    # 🌫️ AIR POLLUTION
    if aqi >= 150:
        amount += 150
        risk_score += 0.2
        reasons.append("High Pollution 🌫️")

    if aqi >= 300:
        amount += 200
        risk_score += 0.3
        reasons.append("Severe Pollution 🚨")

    # 🚫 CURFEW
    if is_curfew:
        amount += 250
        risk_score += 0.4
        reasons.append("Government Curfew 🚫")

    # 📉 LOW DEMAND (reduced impact so it doesn't dominate)
    if orders < 5:
        amount += 50
        risk_score += 0.1
        reasons.append("Low Demand 📉")

    # 🔒 LIMIT VALUES
    risk_score = min(round(risk_score, 2), 1.0)
    amount = min(amount, 700)

    # 🎯 ENSURE MINIMUM IF TRIGGERED
    if amount > 0:
        amount = max(amount, 150)

    # ❌ NO TRIGGER CASE
    if amount == 0:
        return 0, "No threshold crossed", 0

    return amount, ", ".join(reasons), risk_score