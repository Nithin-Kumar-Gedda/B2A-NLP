from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name ='gpt2' # You can specify different GPT Variants
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

prompt = "Once upon a time"
tokens = tokenizer.encode(prompt, return_tensors='pt')
output = model.generate(tokens, max_length= 50, num_return_sequences=1, temperature = 0.9)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated Text:")
print(generated_text)