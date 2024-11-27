from typing import Union
from typing import List
from pathlib import Path

from PyPDF2 import PdfReader



class Pdf:
    
    def __init__(self, file_path: Union[Path, str]) -> None:
        self.file_path = file_path
    

    def read_pdf(self) -> List[str]:
        
        reader = PdfReader(self.file_path)
        pdf_text: str = ""
        
        for page in reader.pages:
            pdf_text += page.extract_text()

        return pdf_text
