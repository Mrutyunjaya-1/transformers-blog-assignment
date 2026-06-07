from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = """
Transformers have revolutionized NLP by introducing self-attention mechanisms and eliminating recurrence.
"""

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True
)

summary_ids = model.generate(
    inputs["input_ids"],
    max_length=50,
    min_length=10
)

summary = tokenizer.decode(
    summary_ids[0],
    skip_special_tokens=True
)

print("Summary:")
print(summary)