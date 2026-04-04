from typing import Optional


# 🔍 ML → RISK SCORE CONVERSION
def calculate_risk_score(premium: float):
    if premium is None:
        return 0.0

    premium = max(0, min(premium, 100))  # safety
    score = premium / 50

    return round(min(score, 1.0), 2)


# 🚦 CLASSIFY RISK
def classify_risk(score: float):
    if score >= 0.7:
        return "HIGH"
    elif score >= 0.4:
        return "MEDIUM"
    else:
        return "LOW"


# 🎯 SMART RECOMMENDATION
def get_recommendation(risk: str, score: Optional[float] = None):

    confidence_base = {
        "LOW": 80,
        "MEDIUM": 85,
        "HIGH": 90
    }

    boost = int(score * 10) if score else 0

    if risk == "LOW":
        return {
            "plan": "Basic",
            "reason": "Low environmental risk",
            "confidence": confidence_base["LOW"] + boost,
            "action": "Normal monitoring"
        }

    elif risk == "MEDIUM":
        return {
            "plan": "Moderate",
            "reason": "Moderate fluctuations detected",
            "confidence": confidence_base["MEDIUM"] + boost,
            "action": "Enable alerts"
        }

    elif risk == "HIGH":
        return {
            "plan": "Premium",
            "reason": "Extreme risk (weather + pollution)",
            "confidence": confidence_base["HIGH"] + boost,
            "action": "Immediate protection needed"
        }

    return {
        "plan": "Unknown",
        "confidence": 0
    }