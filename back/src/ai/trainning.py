import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))


from transformers import LongformerTokenizer, LongformerForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

from ..utils import utils

dataset = load_dataset("csebuetnlp/xlsum", "portuguese")
tokenizer = LongformerTokenizer.from_pretrained("allenai/longformer-base-4096")

def preprocess_data(examples):
    inputs = examples['text']
    targets = examples['summary']
    model_inputs = tokenizer(
        inputs, 
        padding='max_length', 
        truncation=True, 
        max_length=4096,
        return_tensors="pt"
    )
    labels = tokenizer(
        targets, 
        padding='max_length', 
        truncation=True, 
        max_length=512,
        return_tensors="pt"
    )
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs


if __name__ == '__main__':
    from timeit import default_timer
    
    ini_time: float = default_timer()
    utils.add_log.info('[REVIT] Trainning AI starts.')
    
    tokenized_dataset = dataset.map(preprocess_data, batched=True)
    model = LongformerForSequenceClassification.from_pretrained("allenai/longformer-base-4096")

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=1,  # Reduce batch size if necessary
        per_device_eval_batch_size=1,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_dir="./logs",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset['train'],
        eval_dataset=tokenized_dataset['validation'],
    )

    trainer.train()

    end_time: float = default_timer()
    utils.add_log.info(f'[REVIT] Trainning AI ends in {str(round(end_time - ini_time, 2))}.')
