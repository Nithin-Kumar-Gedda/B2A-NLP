import torch
from transformers import BertTokenizer, BertForSequenceClassification

model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Prediction function
def predict_sentiment(sentence):
    tokens = tokenizer(sentence, return_tensors='pt', truncation= True, padding=True, max_length =512)
    with torch.no_grad(): # skips the gradient values/calculations
        outputs = model(**tokens)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return "Positive" if predicted_class ==1 else "Negative"

sentences = [
    "I love this product! It's absolutely wonderful",
    "This is the worst thing I've ever brought.",
    "I'm so happy with the results.",
    "I hate it. It's terrible."
]

for sentence in sentences:
    sentiment = predict_sentiment(sentence)
    print(f"Sentence: {sentence}\nSentiment: {sentiment}\n")