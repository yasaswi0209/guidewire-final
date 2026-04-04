from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ DATABASE URL
DATABASE_URL = "postgresql+psycopg2://postgres:0209@127.0.0.1:5432/ai"

# ✅ ENGINE
engine = create_engine(DATABASE_URL)

# ✅ SESSION
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ✅ BASE (DEFINE ONLY HERE)
Base = declarative_base()


# ✅ DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()