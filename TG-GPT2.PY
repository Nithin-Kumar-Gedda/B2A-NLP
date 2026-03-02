from transformers import GPT2LMHeadModel, GPT2Tokenizer

# load pre-trained model

model_name  = "gpt2"  # we use other size models like "-medium, -large or -xl"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# prompt

prompt = " Once upon a time"

input_data = tokenizer.encode(prompt, return_tensors="pt")

# Generate text
max_length = 100
output = model.generate(input_data, max_length=max_length, num_return_sequences=1, temperature=1.0,do_sample=True, pad_token_id=50256)

# decode nd print generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens= True)

print("Generated text:", generated_text)