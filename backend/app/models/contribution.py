from sqlalchemy import Column, Integer, Float, String
from app.core.database import Base

class Contribution(Base):
    __tablename__ = "contributions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    amount = Column(Float)
    zone = Column(String)