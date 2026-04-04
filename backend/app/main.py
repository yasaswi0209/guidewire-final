from fastapi.middleware.cors import CORSMiddleware



from fastapi import FastAPI
app = FastAPI()

# ✅ ROUTES
try:
    print("🔥 STEP 1 - Importing routes")
    from app.api.routes import risk, claim, payout, settings, auth, insurance
    print("✅ Routes imported")
except Exception as e:
    print("❌ ROUTE IMPORT ERROR:", e)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ DB
try:
    print("🔥 STEP 2 - Importing DB")
    from app.db.session import engine
    print("✅ DB imported")
except Exception as e:
    print("❌ DB ERROR:", e)

# ✅ ATTACH ROUTES
try:
    print("🔥 STEP 3 - Attaching routes")
    app.include_router(auth.router, prefix="/auth", tags=["Auth"])
    app.include_router(risk.router, prefix="/risk", tags=["Risk"])
    app.include_router(claim.router)
    app.include_router(payout.router, tags=["Payout"])
    app.include_router(settings.router)
    print("✅ Routes attached")
except Exception as e:
    print("❌ ROUTER ATTACH ERROR:", e)

print("🔥 STEP 4 - APP READY")

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}