from sqlalchemy import Column, Integer, Float, String
from app.core.database import Base

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    date = Column(String)
    earnings = Column(Float)
    orders_completed = Column(Integer)