from transformers import MBart50Tokenizer, MBartForConditionalGeneration
from langdetect import detect

model_name = 'facebook/mbart-large-50-many-to-many-mmt'
tokenizer = MBart50Tokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

text = input("Text: ")
target = input("Select Translated language keyword(en,fr,de,hi,es) :")

detect_lang = detect(text)
print("Detected language:",detect_lang)

tokenizer.src_lang = detect_lang + "_XX"
encode = tokenizer(text, return_tensors='pt')
generated_tokens = model.generate(**encode,forced_bos_token_id=tokenizer.lang_code_to_id[detect_lang + "_XX"])
translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

# tokens = tokenizer(input, return_tensors='pt', padding=True, truncation = True)
# translation = model.generate(**tokens)
# translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)

print(f"Translated Text : {translated_text}")
