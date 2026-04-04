from sqlalchemy import Column, Integer, Float, String
from app.db.session import Base
class Payout(Base):
    __tablename__ = "payouts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    amount = Column(Float)
    reason = Column(String)