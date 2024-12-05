import sys
import os
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))

import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

from schemas.revit_schema import RevitBase


MODEL_NAME: str = "unicamp-dl/ptt5-base-portuguese-vocab"


class RevitAi:
    
    def __init__(self):
        """
        Inicializa o pipeline de resumo usando o Hugging Face.
        """
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
        self.summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)


    def clean_text(self, text: str) -> str:
        """
        Remove quebras de linha e espaços extras.
        """
        return re.sub(r'\s+', ' ', text.replace('\n', ' ').strip())
    

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


    def chunk_text(self, text: str) -> list:
        # Tokeniza o texto em sentenças usando o NLTK para o idioma português
        sentences = nltk.sent_tokenize(text, language="portuguese")
        
        # Calcula o número de sentenças por chunk
        chunk_size = len(sentences) // 3
        chunks = []

        # Divide o texto em partes
        for i in range(3):
            start_index = i * chunk_size
            end_index = (i + 1) * chunk_size if i != 3 - 1 else len(sentences)
            chunk = ' '.join(sentences[start_index:end_index])
            chunks.append(chunk)

        print(chunks)
        return len(chunks), chunks



    def summarize(self, text: str, max_length: int = None, min_length: int = None) -> str:
        """
        Resume o texto ajustando dinamicamente o comprimento.
        """
        input_length = len(text.split())
        if not max_length:
            max_length = min(300, max(50, int(input_length * 0.5)))  # Máximo: 50% do texto original ou até 300 tokens.
        if not min_length:
            min_length = max(30, int(max_length * 0.3))  # Mínimo: 30% do `max_length`.

        result = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False,
        )
        return result[0]["summary_text"]



    def summarize_large_text(self, text: str) -> str:
        """
        Processa textos longos dividindo em partes menores e gerando um resumo coeso.
        """
        chunk_count, chunks = self.chunk_text(self.clean_text(text))
        summaries = [self.summarize(chunk) for chunk in chunks]
        final_summary = self.summarize(' '.join(summaries))
        return chunk_count, final_summary
