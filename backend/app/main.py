print("APP STARTING DEBUG...")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ IMPORTS (NO TRY CATCH)
from app.api.routes import risk, claim, payout, settings, auth, insurance

from app.db.base import Base
from app.db.session import engine

print("ALL ROUTES IMPORTED SUCCESSFULLY")

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ INCLUDE ROUTES (NO TRY)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(insurance.router)
app.include_router(risk.router, prefix="/risk", tags=["Risk"])
app.include_router(claim.router)
app.include_router(payout.router, tags=["Payout"])
app.include_router(settings.router)

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}