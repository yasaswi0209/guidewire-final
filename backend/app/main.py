from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://guidewire-final.vercel.app",  # ✅ ADD THIS
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES
from app.api.routes.auth import router as auth_router
from app.api.routes.risk import router as risk_router
from app.api.routes.claim import router as claim_router
from app.api.routes.payout import router as payout_router
from app.api.routes.settings import router as settings_router

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(risk_router, prefix="/risk", tags=["Risk"])
app.include_router(claim_router)
app.include_router(payout_router, tags=["Payout"])
app.include_router(settings_router)

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}