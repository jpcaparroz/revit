from pydantic import BaseModel


class HttpDetail(BaseModel):
    detail: str
