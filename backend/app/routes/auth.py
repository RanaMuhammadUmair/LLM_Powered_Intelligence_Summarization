from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from jose import jwt
from datetime import datetime, timedelta
from app.database import SessionLocal
from app.models.schemas import User
import os

router = APIRouter()
JWT_SECRET = os.getenv("JWT_SECRET")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = bcrypt.hash(password)
    new_user = User(email=email, password_hash=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not bcrypt.verify(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    payload = {
        "user_id": str(user.id),
        "email": user.email,
        "role": user.role,
        "exp": datetime.utcnow() + timedelta(hours=12)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return {"access_token": token}
