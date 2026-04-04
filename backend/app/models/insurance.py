from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db.session import Base


class Insurance(Base):
    __tablename__ = "insurance"

    id = Column(Integer, primary_key=True, index=True)

    # 🔗 User relation
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # 📦 Plan details
    plan_name = Column(String, nullable=False)
    premium = Column(Integer, nullable=False)   # 💰 weekly price
    coverage = Column(Integer, nullable=False)  # 🛡️ coverage amount

    # 📊 Status
    status = Column(String, default="ACTIVE")

    # 🔒 Lock system (VERY IMPORTANT)
    locked_until = Column(DateTime, nullable=True)

    # 🕒 Optional (good for tracking)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())