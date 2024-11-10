import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))

from transformers import AutoTokenizer, Trainer, TrainingArguments, LEDForConditionalGeneration
from datasets import load_dataset
import numpy as np
import evaluate
import torch
    
from ..utils import utils

dataset = load_dataset("csebuetnlp/xlsum", "portuguese")
tokenizer = AutoTokenizer.from_pretrained("allenai/longformer-base-4096")

def tokenize_function(examples):
    inputs = examples['text']
    targets = examples['summary']
    
    model_inputs = tokenizer(
        inputs, 
        padding='max_length', 
        truncation=True, 
        max_length=2048,
        return_tensors="pt"
    )
    
    labels = tokenizer(
        targets, 
        padding='max_length', 
        truncation=True, 
        max_length=512,  # Adjust the max length as needed
        return_tensors="pt"
    )
    model_inputs["labels"] = labels["input_ids"]
    
    return model_inputs

# Define metrics
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = logits.argmax(dim=-1)
    rouge = evaluate.load("rouge")
    return rouge.compute(predictions=predictions, references=labels)


if __name__ == '__main__':
    from timeit import default_timer
    
    torch.cuda.empty_cache()
    
    ini_time: float = default_timer()
    utils.add_log.info('[REVIT] Training AI starts.')
    
    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    model = LEDForConditionalGeneration.from_pretrained("allenai/longformer-base-4096")
    metric = evaluate.load("rouge")
    
    # Set training arguments
    training_args = TrainingArguments(
        output_dir="./ai/results-v2",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=4, 
        num_train_epochs=3,
        max_steps=2000,
        weight_decay=0.01,
        logging_dir="./ai/results-v2/logs",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset['train'],
        eval_dataset=tokenized_dataset['validation'],
        compute_metrics=compute_metrics
    )

    try:
        trainer.train()
    except Exception as e:
        utils.add_log.error(f'[REVIT] Training AI finish with errors: {str(e)}')    

    end_time: float = default_timer()
    utils.add_log.info(f'[REVIT] Training AI ends in {str(round(end_time - ini_time, 2))}.')
