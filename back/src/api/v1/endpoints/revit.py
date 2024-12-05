import time
from io import BytesIO

from fastapi import HTTPException, UploadFile, APIRouter
from fastapi import status

from schemas.revit_schema import RevitBase
from functions.pdf_reader import Pdf
from functions.ai_summarize import RevitAi


router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK, response_model=RevitBase)
async def summarize(file: UploadFile):
    start_time = time.time()

    try:
        file_read = BytesIO(await file.read())
        pdf_reader = Pdf(file_read)
        text: str = pdf_reader.read_pdf()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Error on file read')
        
    try:
        revit = RevitAi()
        chunk_count, summarize_result = revit.summarize_large_text(text)
        
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f'Error on summarize PDF. Error {str(e)}')
        
    end_time = time.time()
    duration_seconds = int(end_time - start_time)
    hours, remainder = divmod(duration_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    duration = f"{hours:02}:{minutes:02}:{seconds:02}"
    
    revit_dict = {
        "file_name": str(file.filename),
        "file_content": text,
        "file_chars_count": len(text),
        "file_chunks_count": chunk_count,
        "summary": summarize_result,
        "summarize_duration": duration,
        "summarize_chars_count": len(summarize_result)
    }
    revit_schema = revit.revit_message(RevitBase(**revit_dict))
        
    return revit_schema
