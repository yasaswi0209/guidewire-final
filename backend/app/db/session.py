from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base

# ✅ CHANGE THIS TO YOUR POSTGRES URL
DATABASE_URL = "postgresql+psycopg2://postgres:0209@127.0.0.1:5432/ai"
# ✅ ENGINE (THIS WAS MISSING ❌)
engine = create_engine(DATABASE_URL)

# ✅ SESSION
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ✅ DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()