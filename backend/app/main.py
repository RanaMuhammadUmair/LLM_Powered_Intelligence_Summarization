# backend/app/main.py
from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth


app = FastAPI()
# Create tables (optional, only for first-time setup)
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "LLM Backend running"}


