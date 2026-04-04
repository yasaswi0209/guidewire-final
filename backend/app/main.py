from fastapi import FastAPI

from app.api.routes import risk, claim, payout, settings, auth, insurance
from app.db.session import engine

app = FastAPI()

# ✅ Attach routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(risk.router, prefix="/risk", tags=["Risk"])
app.include_router(claim.router)
app.include_router(payout.router, tags=["Payout"])
app.include_router(settings.router)

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}