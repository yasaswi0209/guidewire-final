from sqlalchemy import Column, Integer, String
from app.db.base import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    # ✅ NEW FIELDS
    platform = Column(String, nullable=False)
    location = Column(String, nullable=False)
    weekly_income = Column(Integer, nullable=False)