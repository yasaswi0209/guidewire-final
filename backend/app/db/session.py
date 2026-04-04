from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv


load_dotenv()  # 🔥 THIS IS THE FIX
# ✅ GET FROM RENDER ENV
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

# ✅ FIX postgres:// issue (Render uses this sometimes)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# ✅ ENGINE WITH SSL (RENDER NEEDS THIS)
# ✅ ENGINE (SMART FIX)
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL)
else:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"sslmode": "require"}
    )

# ✅ SESSION
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ✅ BASE
Base = declarative_base()

# ✅ DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()