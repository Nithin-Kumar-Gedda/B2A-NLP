from transformers import pipeline
import string
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy 


classifier = pipeline("sentiment-analysis")  ## model

with open("sample.txt","r") as file:  ## reading file
    text = file.read()

for p in string.punctuation:   ## removing punctuations
    text = text.replace(p,"")

# result = classifier(text)
# words = text.split()

# print("Sentiment:",result[0]['label'])
# print("Confidence",result[0]['score'])
# print("Number of Words:",len(words))

# sentences = sent_tokenize(text)
# words = word_tokenize(text)

nlp = spacy.load("en_core_web_sm")  #spacy model
doc = nlp(text)

sentences = [sent.text for sent in doc.sents]
words = [token.text for token in doc]

print(text)
print("Sentences:",sentences)
print("Words:",words)