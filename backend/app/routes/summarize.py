from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.llm import summarize_text

router = APIRouter()

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
