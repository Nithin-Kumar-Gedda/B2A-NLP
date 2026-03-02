import torch
from transformers import GPT2LMHeadModel,GPT2Tokenizer

# 1. Load Pretrained Model

model_name = "gpt2"   # Use Large or Xl models generate text that makes more sense and reads smoothly, maintaining logical flow and context..
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# 2. User Preferences

destination = input("Enter destination: ")
days = input("Enter number of days: ")
budget = input("Enter budget (low / medium / high ): ")
interests = input("enter interests: ")

# 3. Create Prompt Dynamically

prompt = f"""
Create a detailed {days}-day travel itinerary for {destination}.
Budget level: {budget}
Interets: {interests}

Include:
1. Daily activities (clearly separated by day)
2. Hotel recommandations
3. Travel tips

Format with proper headings.
"""

# 4. Tokenize

input_ids = tokenizer.encode(prompt, return_tensors='pt')

# 5. Generate AI Output

output = model.generate(input_ids, max_length= 500, 
                        temperature=1.0,
                        do_sample=True,
                        top_p = 0.9, 
                        # pad_token_id = tokenizer.eos_taken_id
                        )

# 6. Decode & Output

generated_text = tokenizer.decode(output[0], skip_special_tokens = True)

print("===== Travel Itinerary =====")
print(generated_text)