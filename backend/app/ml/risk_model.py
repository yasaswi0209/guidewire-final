# app/ml/risk_model.py

def calculate_risk(income: float, claims: int, trust_score: float):
    score = 0

    # simple logic (you can improve later)
    if income < 20000:
        score += 2
    if claims > 3:
        score += 2
    if trust_score < 50:
        score += 2

    # risk decision
    if score >= 4:
        return "High"
    elif score >= 2:
        return "Medium"
    else:
        return "Low"