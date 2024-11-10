import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))

from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer


class RevitIa:
    
    model = AutoModelForSeq2SeqLM.from_pretrained("../ai/results/checkpoint-1500")
    tokenizer = AutoTokenizer.from_pretrained("allenai/longformer-base-4096")


    def test_summarize(self, text: str,
                             max_length: int = 150, 
                             min_length: int = 30) -> str:
        
        inputs = self.tokenizer(
            text, 
            max_length=max_length, 
            truncation=True, 
            return_tensors="pt"
        )
        
        summary_ids = self.model.generate(
            inputs["input_ids"],
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )

        summary = self.tokenizer.decode(summary_ids[0], 
                                        skip_special_tokens=True)

        return summary
