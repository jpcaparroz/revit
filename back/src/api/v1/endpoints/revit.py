from typing import List
from io import BytesIO

from fastapi import HTTPException
from fastapi import UploadFile
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from schemas.generic_schema import HttpDetail
from functions.pdf_reader import Pdf


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_hello_world():
    return HttpDetail(detail='Hello World!')


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
