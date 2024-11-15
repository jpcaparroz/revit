from pydantic import BaseModel
from typing import Optional


class RevitBase(BaseModel):
    file_name: str
    file_content: str
    file_chars_count: int
    file_chunks_count: Optional[int] = 0
    summary: str
    summarize_duration: str
    summarize_chars_count: int
    revit_summary_message: Optional[str] = None
