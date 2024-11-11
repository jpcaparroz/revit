from pydantic import BaseModel
from typing import Optional


class RevitBase(BaseModel):
    file_name: str
    file_content: str
    file_words_count: int
    summary: str
    summarize_duration: str
    summarize_words_count: int
    revit_summary_message: Optional[str] = None
