import time
from io import BytesIO

from fastapi import HTTPException
from fastapi import UploadFile
from fastapi import APIRouter
from fastapi import status

from schemas.generic_schema import HttpDetail
from schemas.revit_schema import RevitBase
from functions.pdf_reader import Pdf
from functions.ai_summarize import RevitAi


router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK, response_model=RevitBase)
async def summarize(file: UploadFile):
    start_time = time.time()  # Record the start time

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
        #summarize_final_result = revit.summarize(summarize_result)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Error on summarize PDF')
        
    end_time = time.time()  # Record the end time
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


@router.post("/read_pdf", status_code=status.HTTP_200_OK)
async def get_pdf_full_text(file: UploadFile):
    
    try:
        file_read = BytesIO(await file.read())
        pdf_reader = Pdf(file_read)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Erro on file read')
    
    return HttpDetail(detail=pdf_reader.read_pdf())


@router.get("/lorem-ipsum", status_code=status.HTTP_200_OK)
async def get_lorem_ipsum():
    
    lorem: str = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type 
    specimen book. It has survived not only five centuries, but also the leap into 
    electronic typesetting, remaining essentially unchanged. It was popularised in 
    the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
    and more recently with desktop publishing software like Aldus PageMaker including 
    versions of Lorem Ipsum.
    """
    return HttpDetail(detail=lorem)
