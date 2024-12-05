import sys
import os
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from schemas.revit_schema import RevitBase


MODEL_NAME = "csebuetnlp/mT5_multilingual_XLSum"


class RevitAi:
    def __init__(self):
        """
        Inicializa o modelo e o tokenizador do Hugging Face.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    def clean_text(self, text: str) -> str:
        """
        Remove quebras de linha e espaços extras.
        """
        return re.sub(r'\s+', ' ', text.replace('\n', ' ').strip())

    def revit_message(self, revit: RevitBase) -> str:
        """
        Prepara mensagem final de resposta da sumarização.
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

    def chunk_text(self, text: str, max_tokens: int = 256):
        """
        Divide o texto em chunks com base no número máximo de tokens permitido.
        """
        tokens = self.tokenizer.encode(text, truncation=False)
        chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]

        result = [self.tokenizer.decode(chunk, skip_special_tokens=True) for chunk in chunks]
        return len(chunks), result

    def summarize(self, text: str, max_length: int = None, min_length: int = None) -> str:
        """
        Resume o texto dado usando o modelo.
        """
        inputs = self.tokenizer.encode(text, return_tensors='pt', truncation=True, max_length=512)

        # Define valores padrão para max_length e min_length
        max_length = max_length or min(300, int(len(inputs[0]) * 0.5))
        min_length = min_length or max(30, int(max_length * 0.3))

        # Gera o resumo
        summary_ids = self.model.generate(
            inputs,
            max_length=max_length,
            min_length=min_length,
            num_beams=5,
            no_repeat_ngram_size=3,
            early_stopping=True,
        )
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

    def summarize_large_text(self, text: str) -> str:
        """
        Processa textos longos dividindo em chunks menores e gerando um resumo coeso.
        """
        chunk_count, chunks = self.chunk_text(self.clean_text(text))
        summaries = [self.summarize(chunk) for chunk in chunks]

        # Realiza uma segunda rodada de sumarização no resumo combinado
        final_summary = ' '.join(summaries)
        return chunk_count, final_summary
