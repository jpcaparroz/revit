import sys
import os
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))

from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer, T5Tokenizer

from schemas.revit_schema import RevitBase

MODEL_NAME: str = "csebuetnlp/mT5_multilingual_XLSum"
WHITESPACE_HANDLER = lambda k: re.sub('\\s+', ' ', re.sub('\n+', ' ', k.strip()))

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
        Quantidade de Caracteres de Origem: {revit.file_words_count}
        Duração da Criação do Resumo: {revit.summarize_duration}
        Quantidade de Caracteres do Resumo: {revit.summarize_words_count}
        """
        
        revit.revit_summary_message = message
        return revit


    def summarize(self, text: str) -> str:
        
        input_ids = self.tokenizer(
            [WHITESPACE_HANDLER(text)],
            return_tensors="pt",
            padding="max_length",
            truncation=True,
            max_length=2048
        )["input_ids"]
        
        output_ids = self.model.generate(
            input_ids=input_ids,
            max_length=1024,
            no_repeat_ngram_size=2,
            num_beams=4
        )[0]
        
        summary = self.tokenizer.decode(
            output_ids,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False
        )

        return summary
