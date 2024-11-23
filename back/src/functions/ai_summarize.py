import sys
import os
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))

from transformers import pipeline

from schemas.revit_schema import RevitBase

MODEL_NAME: str = "csebuetnlp/mT5_multilingual_XLSum"
WHITESPACE_HANDLER = lambda k: re.sub(r'\s+', ' ', re.sub('\n+', ' ', k.strip()))

class RevitAi:
    
    def __init__(self):
        """
        Inicializa o pipeline de resumo usando o Hugging Face.
        """
        self.summarizer = pipeline("summarization", model=MODEL_NAME)


    def revit_message(self, revit: RevitBase) -> str:
        """
        Prepara mensagem final de resposta da sumarizacão.
        """
        message: str = f"""
        Olá, eu sou o Revit! Construído pela Loopdevs para resumir seus PDFs.
        Abaixo mandarei o resumo do seu arquivo "{revit.file_name}" =)
        
        Resumo:
        {revit.summary}
        
        Detalhes:

        Nome do Arquivo: {revit.file_name}
        Quantidade de Caracteres de Origem: {revit.file_chars_count}
        Quantidade de Chunks Criados: {revit.file_chunks_count}
        Duração da Criação do Resumo: {revit.summarize_duration}
        Quantidade de Caracteres do Resumo: {revit.summarize_chars_count}
        """
        
        revit.revit_summary_message = message
        return revit


    def chunk_text(self, text: str):
        """
        Separa o texto em pedacos caso ele seja maior que 1500 ou por paragrafos.
        """
        paragraphs = text.split('\n')  # Dividindo por parágrafos

        chunk_size = 0
        chunks = []
        current_chunk = []

        for paragraph in paragraphs:
            current_chunk.append(paragraph)
            chunk_size += len(paragraph)

            if chunk_size > 1500:  # Ajuste o limite conforme necessário
                chunks.append("\n".join(current_chunk))
                current_chunk = []
                chunk_size = 0

        if current_chunk:
            chunks.append("\n".join(current_chunk))

        return chunks


    def summarize(self, text: str) -> str:
        """
        Resume o texto enviado.
        """
        result = self.summarizer([WHITESPACE_HANDLER(text)], max_length=130, min_length=50, do_sample=False)
        return result[0]["summary_text"]


    def summarize_large_text(self, text: str) -> str:
        """
        Resume textos maiores separando-o em pedacos.
        """
        chunks: list = self.chunk_text(text)
        summaries: list = []
        chunk_count: int = 0
        
        if len(chunks) > 5:
            for chunk in chunks:
                summary = self.summarize(chunk)
                summaries.append(summary)
                chunk_count += 1
                
            final_summary = self.summarize(" ".join(summaries))
        else:
            final_summary = self.summarize(text)

        return chunk_count, final_summary
