from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.llm import summarize_text

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.schemas import Summary
from jose import jwt, JWTError
import os
import uuid
import requests


router = APIRouter()
JWT_SECRET = os.getenv("JWT_SECRET")

@router.post("/")
async def summarize(
    file: UploadFile = File(...),
    model: str = Form(...)
):
    try:
        content = await file.read()
        text = content.decode("utf-8", errors="ignore")
        summary = await summarize_text(text, model)
        return {"summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/summarize")
def summarize(file_text: str, model: str, token: str, db: Session = Depends(get_db)):
    user = verify_token(token)
    
    # Forward to appropriate model
    if model == "openai":
        summary = call_openai_api(file_text)
    elif model == "deepseek":
        summary = call_deepseek_api(file_text)
    elif model == "runpod":
        summary = call_runpod_model(file_text)
    else:
        raise HTTPException(status_code=400, detail="Model not supported")
    
    # Save in DB
    new_summary = Summary(
        user_id=user["user_id"],
        model=model,
        original_filename="N/A",
        summary_text=summary
    )
    db.add(new_summary)
    db.commit()

    return {"summary": summary}

# ================================
# 🔥 Example dummy model calls (replace with real API later)

def call_openai_api(text):
    return f"OpenAI summary of: {text[:30]}"

def call_deepseek_api(text):
    return f"DeepSeek summary of: {text[:30]}"

def call_runpod_model(text):
    return f"RunPod model summary of: {text[:30]}"