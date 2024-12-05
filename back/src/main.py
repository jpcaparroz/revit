from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import get_env_fastapi_config
from core.config import settings
from api.v1.api import router


app = FastAPI(title='Revit')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router, prefix=settings.API_VERSION_ADDRESS)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(**get_env_fastapi_config())
