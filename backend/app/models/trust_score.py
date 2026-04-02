from sqlalchemy import Column, Integer, Float
from app.core.database import Base

class TrustScore(Base):
    __tablename__ = "trust_scores"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    score = Column(Float)