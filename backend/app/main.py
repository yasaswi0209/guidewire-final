print("APP STARTING DEBUG...")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ SAFE IMPORTS
try:
    from app.api.routes import risk, claim, payout, settings, auth, insurance
    print("Routes imported")
except Exception as e:
    print("ROUTE IMPORT ERROR:", e)

try:
    from app.db.base import Base
    from app.db.session import engine
    print("DB imported")
except Exception as e:
    print("DB ERROR:", e)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes (only if import worked)
try:
    app.include_router(auth.router, prefix="/auth", tags=["Auth"])
    app.include_router(insurance.router)
    app.include_router(risk.router, prefix="/risk", tags=["Risk"])
    app.include_router(claim.router)
    app.include_router(payout.router, tags=["Payout"])
    app.include_router(settings.router)
except Exception as e:
    print("ROUTER ATTACH ERROR:", e)

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}