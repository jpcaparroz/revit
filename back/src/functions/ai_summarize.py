import sys
import os
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))

from transformers import AutoModelForSeq2SeqLM
from transformers import T5Tokenizer

from schemas.revit_schema import RevitBase

MODEL_NAME: str = "csebuetnlp/mT5_multilingual_XLSum"
WHITESPACE_HANDLER = lambda k: re.sub(r'\s+', ' ', re.sub('\n+', ' ', k.strip()))

class RevitAi:
    
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)

    
    def revit_message(self, revit: RevitBase) -> str:
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
        # Se a quantidade de texto for muito grande, vamos tentar dividi-la por seções ou parágrafos
        paragraphs = text.split('\n')  # Dividindo por parágrafos

        chunk_size = 0
        chunks = []
        current_chunk = []

        for paragraph in paragraphs:
            current_chunk.append(paragraph)
            chunk_size += len(paragraph)

            # Se o tamanho do chunk ultrapassar um limite, armazene o chunk
            if chunk_size > 1500:  # Ajuste o limite conforme necessário
                chunks.append("\n".join(current_chunk))
                current_chunk = []
                chunk_size = 0

        # Adiciona o último pedaço se houver
        if current_chunk:
            chunks.append("\n".join(current_chunk))

        return chunks


    def summarize(self, text: str) -> str:
        
        input_ids = self.tokenizer(
            WHITESPACE_HANDLER(text),
            return_tensors="pt",
            padding="max_length",
            truncation=True,
            max_length=2048
        )["input_ids"]
        
        output_ids = self.model.generate(
            input_ids=input_ids,
            max_length=2048,
            no_repeat_ngram_size=2,
            num_beams=4
        )[0]
        
        summary = self.tokenizer.decode(
            output_ids,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False
        )
        
        return summary


    def summarize_large_text(self, text: str) -> str:
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
        
        print(text)
        print([WHITESPACE_HANDLER(text)])

        print(final_summary)
        return chunk_count, final_summary
