import nltk
from collections import defaultdict, Counter
import random

nltk.download('punkt')

txt = "I like cats. I like dogs. I like cats more than dogs. cats are cuter"

tokens = nltk.word_tokenize(txt)  # tokenization

bigrams = list(nltk.bigrams(tokens)) # Bigrams
bigram_freq = Counter(bigrams)

unigram_freq = Counter(tokens) #Unigrams count

bigram_prob = defaultdict(lambda: defaultdict(float))
for (w1,w2), freq in bigram_freq.items():
    bigram_prob [w1][w2] = freq/unigram_freq[w1]

def predict_nxt_word(current_word, bigram_prob):
    if current_word in bigram_prob:
        next_word_prob = bigram_prob[current_word]
        next_word = max(next_word_prob,key = next_word_prob.get)
        return next_word
    else:
        return None

current_word = "like"
next_word = predict_nxt_word(current_word, bigram_prob)
print(f"The next word after '{current_word}' is '{next_word}'.") 





