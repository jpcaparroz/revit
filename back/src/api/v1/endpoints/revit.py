from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi import status

from schemas.generic_schema import HttpDetail


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_hello_world():
    return HttpDetail(detail='Hello World!')
