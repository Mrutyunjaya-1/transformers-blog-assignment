from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = "Machine learning is transforming industries."

inputs = tokenizer(
    text,
    return_tensors="pt"
)

translated = model.generate(**inputs)

output = tokenizer.decode(
    translated[0],
    skip_special_tokens=True
)

print("Translation:")
print(output)