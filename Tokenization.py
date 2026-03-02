import nltk
nltk.download('wordnet')
from nltk.tokenize import punkt

text = 'This is an example of text tokenization, a small sentence though.'

tokenizer = punkt.PunktLanguageVars()
tokens = tokenizer.word_tokenize(text)

for token in tokens:
    print(token)