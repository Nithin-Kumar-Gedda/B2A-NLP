# Statistical-Based NLG System

import random
from collections import defaultdict

corpus = [
    "machine learning is a subset of artificial intelligence.",
    "artificial intelligence is transforming many industries",
    "many industries use machine learning techniques",
    "machine learning techniques include supervised learning",
    "supervised learning and unsupervised learning are popular methods",
    "deep learning is a subset of machine learning",
    "deep learning techniques are used in computer vision",
    "computer vision is a branch of artificial intelligence",
    "natural language processing is a branch of artificial intelligence",
    "natural language processing uses machine learning models"
]

# function to build the n-gram model

def build_ngram_model(corpus, n):
    model = defaultdict(lambda: defaultdict(lambda: 0))
    for sentence in corpus:
        tokens = sentence.split()
        for i in range (len(tokens)-n):
            ngram = tuple(tokens[i:i+n])
            next_token = tokens[i+n]
            model[ngram][next_token] +=1
    return model

#Function to generate text

def generate_text(model, n, length=10):
    start = random.choice(list(model.keys()))
    result = list(start)
    for _ in range(length-n):
        ngram = tuple(result[-n:])
        if ngram in model:
            next_token = random.choices(list(model[ngram].keys()),list(model[ngram].values()))[0]
            result.append(next_token)
        else:
            break
    return " ".join(result)

ngram_model = build_ngram_model(corpus, 2)
generated_text = generate_text(ngram_model, 2, length=10)
print("Generated text:", generated_text)