def process_payout(user_id: int, loss: float):
    if loss > 500:
        return {
            "status": "APPROVED",
            "amount": loss
        }
    return {
        "status": "REJECTED",
        "amount": 0
    }