# app/ml/claim_model.py

def evaluate_claim(risk: str, ml_score: float, claim_amount: float):

    # 🟢 AUTO CLAIM
    if risk == "LOW" and ml_score < 0.6 and claim_amount <= 5000:
        return {
            "status": "AUTO_APPROVED",
            "amount": claim_amount,
            "message": "Auto claim processed instantly 🚀",
            "fraud": False
        }

    # 🟡 NORMAL APPROVAL
    elif risk == "MEDIUM" and ml_score < 0.7:
        return {
            "status": "APPROVED",
            "amount": int(claim_amount * 0.8),
            "message": "Partially approved",
            "fraud": False
        }

    # 🔴 REJECT
    else:
        return {
            "status": "REJECTED",
            "amount": 0,
            "message": "High risk detected",
            "fraud": True
        }
    """
    Auto claim decision engine
    """

    # 🚨 HIGH RISK → reject or manual review
    if risk == "HIGH":
        if claim_amount > 5000:
            return {
                "status": "REJECTED",
                "reason": "High risk + high claim amount"
            }
        else:
            return {
                "status": "MANUAL_REVIEW",
                "reason": "High risk user"
            }

    # ⚠️ MEDIUM RISK → partial approval logic
    elif risk == "MEDIUM":
        if ml_score > 0.7:
            return {
                "status": "MANUAL_REVIEW",
                "reason": "ML detected high risk pattern"
            }
        else:
            return {
                "status": "APPROVED",
                "amount_approved": claim_amount * 0.8,
                "reason": "Partial approval"
            }

    # ✅ LOW RISK → auto approve
    elif risk == "LOW":
        return {
            "status": "APPROVED",
            "amount_approved": claim_amount,
            "reason": "Low risk user"
        }

    # fallback
    return {
        "status": "MANUAL_REVIEW",
        "reason": "Unknown condition"
    }
