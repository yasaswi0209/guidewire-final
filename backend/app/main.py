from fastapi import FastAPI

print("🔥 MAIN STARTED")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}