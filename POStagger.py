import nltk
from nltk.tokenize import punkt
import spacy
from textblob import TextBlob


# Average Perceptron Tgger in NLTK

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "I am learning NLP in python"
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)

# en_core_web_sm tagger in spacy

nlp = spacy.load('en_core_web_sm')
sentence1 = "This chapter is about lexical analysis"
doc = nlp(sentence1)
for token in doc:
    print(token.text, token.pos_)

# textBLOB tagger 

sentence2 = "This chapter is about lexical analysis"
text_bolb = TextBlob(sentence2)
pos_tag = text_bolb.tags
print(pos_tag)