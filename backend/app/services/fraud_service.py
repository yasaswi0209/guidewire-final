def check_fraud(user_id: int, amount: float, risk_score: float):
    """
    Intelligent fraud detection logic
    Returns:
        (is_fraud: bool, reason: str)
    """

    # 🚨 Rule 1: Extreme risk
    if risk_score >= 0.95:
        return True, "Extreme risk score 🚨"

    # 🚨 Rule 2: Very high payout
    if amount >= 500:
        return True, "Unusually high payout 💰"

    # 🚨 Rule 3: Suspicious combination
    if risk_score > 0.7 and amount > 300:
        return True, "High risk + high payout ⚠️"

    # 🚨 Rule 4: Low activity but high claim
    if risk_score > 0.6 and amount > 250:
        return True, "Mismatch between activity & claim 📉"

    # ✅ Safe
    return False, "Legitimate claim ✅"