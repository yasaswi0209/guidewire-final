from sqlalchemy import Column, Integer, Float, String
from app.core.database import Base

class CommunityPool(Base):
    __tablename__ = "community_pools"

    id = Column(Integer, primary_key=True, index=True)
    zone = Column(String)
    total_funds = Column(Float, default=0.0)