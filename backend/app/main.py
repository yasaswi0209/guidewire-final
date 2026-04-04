from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all routers
from app.api.routes import auth, insurance, risk, claim, payout, settings

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(insurance.router)
app.include_router(claim.router)
app.include_router(payout.router, tags=["Payout"])
app.include_router(settings.router)

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}