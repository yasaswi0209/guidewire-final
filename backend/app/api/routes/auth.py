from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()

@router.get("/")
def test_auth(db: Session = Depends(get_db)):
    return {"message": "auth + db working"}