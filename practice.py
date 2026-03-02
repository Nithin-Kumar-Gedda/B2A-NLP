import nltk
from collections import Counter, defaultdict

nltk.download('punkt')

txt ="the cat sat on the mat"
tokens = nltk.word_tokenize(txt)

bigrams = list(nltk.bigrams(tokens))
bigram_freq = Counter(bigrams)

unigram_freq = Counter(tokens)

bigram_prob = defaultdict(lambda: defaultdict(float))
for (w1,w2), freq in bigram_freq.items():
    bigram_prob [w1][w2] = freq / unigram_freq[w1]

sentence_prob = 1

for w1, w2 in bigrams:
    sentence_prob *= bigram_prob[w1][w2]

print("Sentence probability:",sentence_prob)
