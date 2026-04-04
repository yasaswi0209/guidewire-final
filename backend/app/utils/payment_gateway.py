import razorpay
import os
import random
from datetime import datetime

# 🔐 Use environment variables in production
RAZORPAY_KEY = os.getenv("RAZORPAY_KEY", "rzp_test_SZGdtReidYzj4U")
RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET", "YYPVSlIl7Ir57reU7lq36WHG")

client = razorpay.Client(auth=(RAZORPAY_KEY, RAZORPAY_SECRET))


def process_payout(user_id: int, amount: float):
    """
    💸 Send insurance claim payout via Razorpay (UPI test mode)
    """

    try:
        response = client.payout.create({
            "account_number": "23232300000001",  # ✅ demo account number
            "fund_account": {
                "account_type": "vpa",
                "vpa": {
                    "address": "success@razorpay"  # ✅ always success in test mode
                }
            },
            "amount": int(amount * 100),  # ₹ → paise
            "currency": "INR",
            "mode": "UPI",
            "purpose": "payout",
            "queue_if_low_balance": True,
            "reference_id": f"claim_{user_id}",
            "narration": "Insurance Claim Payout"
        })

        print("✅ PAYMENT SUCCESS:", response)

        return {
            "status": "success",
            "provider": "Razorpay",
            "method": "UPI",
            "id": response.get("id") or f"rzp_demo_{random.randint(10000,99999)}",  # 🔥 fallback
            "time": datetime.now().strftime("%d %b %Y, %I:%M %p")
        }

    except Exception as e:
        print("❌ PAYMENT FAILED:", str(e))

        return {
            "status": "failed",
            "provider": "Razorpay",
            "method": "UPI",
            "id": f"rzp_fail_{random.randint(10000,99999)}",  # 🔥 even on fail show ID
            "time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
            "error": str(e)
        }