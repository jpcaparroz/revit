from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from transformers import pipeline


class RevitIa:
    
    def summarize(self, text: str,
                        max_length: int = 150, 
                        min_length: int = 30) -> str:

        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)

        return summary
    
    def test_summarize(self, text: str,
                             max_length: int = 150, 
                             min_length: int = 30) -> str:
        
        tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
        model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
        
        inputs = tokenizer(
            text, max_length=max_length, truncation=True, return_tensors="pt"
        )  # Limiting to 1024 tokens to fit model requirements

        # Step 4: Generate summary
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=max_length,
            min_length=30,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )

        # Step 5: Decode the summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary
