from fastapi import APIRouter

from api.v1.endpoints import revit


router = APIRouter()
router.include_router(revit.router, prefix='/revit', tags=['Revit'])
