from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import risk   # ✅ ADD THIS
from app.db.base import Base
from app.db.session import engine
from app.api.routes import claim
from app.api.routes import payout
from app.api.routes import settings



# ✅ Load models
from app.models.user import User
from app.models.insurance import Insurance   # 🔥 IMPORTANT (ensure table creation)

# Routes
from app.api.routes import auth, insurance

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",   # ✅ allows ALL origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Create tables
Base.metadata.create_all(bind=engine)

# ✅ Routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(insurance.router)
app.include_router(risk.router, prefix="/risk", tags=["Risk"])
app.include_router(claim.router)
app.include_router(payout.router, tags=["Payout"])


app.include_router(settings.router)
@app.get("/")
def root():
    return {"message": "Backend running 🚀"}