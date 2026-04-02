from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Insurance(Base):
    __tablename__ = "insurance"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    plan_name = Column(String)
    premium = Column(Integer)
    coverage = Column(Integer)

    status = Column(String, default="ACTIVE")