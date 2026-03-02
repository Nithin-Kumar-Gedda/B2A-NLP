import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

text = 'Let us see how the stop words removal works.'

tokens = word_tokenize(text)

filtered_words =[]
removed_words =[]

for w in tokens:
    if w not in stop_words:
        filtered_words.append(w)
    else:
        removed_words.append(w)

print('Original Sentence', tokens)
print('After removing stop words', filtered_words)
print('Removed words', removed_words)