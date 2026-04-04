from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class UserBank(Base):
    __tablename__ = "user_bank"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    name = Column(String)     # ✅ REQUIRED
    phone = Column(String)    # ✅ REQUIRED
    upi = Column(String)      # ✅ REQUIRED