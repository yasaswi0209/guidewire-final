from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.db.session import Base


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    trigger_type = Column(String, nullable=True)

    # 🤖 AI metrics
    risk_score = Column(Float, default=0.0)
    risk_level = Column(String, default="low")   # ✅ NEW

    # 💸 payout
    amount = Column(Float, default=0.0)

    # 🚨 fraud + status
    status = Column(String, default="pending")
    is_fraud = Column(Boolean, default=False)
    fraud_reason = Column(String, nullable=True)  # ✅ NEW

    # 💳 payment info
    payment_status = Column(String, default="pending")  # ✅ NEW
    payment_id = Column(String, nullable=True)          # ✅ NEW
    payment_method = Column(String, default="UPI")      # ✅ NEW
    payment_provider = Column(String, default="Razorpay")  # ✅ NEW

    created_at = Column(DateTime, default=datetime.utcnow)