import time

from fastapi import HTTPException
from fastapi import APIRouter
from fastapi import status
from fastapi import Query

from functions.ai_summarize import RevitAi


router = APIRouter()

from pydantic import BaseModel
from typing import Optional


class RevitBase(BaseModel):
    time: str
    chunks: int
    result_ai: str
    

@router.post("/", status_code=status.HTTP_200_OK)
async def test_summarize(text: str = Query):
    start_time = time.time()
    
    try:
        revit = RevitAi()
        chunks, summary = revit.summarize_large_text(text)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f'Error on summarize PDF. Error: {str(e)}')
        
    end_time = time.time()
    duration_seconds = int(end_time - start_time)
    hours, remainder = divmod(duration_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    duration = f"{hours:02}:{minutes:02}:{seconds:02}"
        
    return RevitBase(time=duration, chunks=chunks, result_ai=summary)
