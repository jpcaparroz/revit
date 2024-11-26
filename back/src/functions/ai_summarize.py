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
        paragraphs = text.split('. ')  # Dividindo por pontos
        chunk_size = len(paragraphs)

        return chunk_size, paragraphs


    def summarize(self, max_length: int, text: str) -> str:
        """
        Resume o texto enviado.
        """
        result = self.summarizer(WHITESPACE_HANDLER(text), max_length=max_length, min_length=50, do_sample=False)
        
        return result[0]["summary_text"]


    def summarize_large_text(self, text: str) -> str:
        """
        Resume textos maiores separando-o em pedacos.
        """
        chunk_count, treated_text = self.chunk_text(text)
        summaries = []
        
        for chunk in treated_text:
            summary = self.summarize(len(chunk), chunk)
            summaries.append(summary)
            chunk_count += 1
            
        final_summary = " ".join(summaries)

        return chunk_count, final_summary
