from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["program","programming","programer","programs","programmed","running", "jumps","happily"]

stem_word = [stemmer.stem(word) for word in words]
lemm_word = [lemmatizer.lemmatize(word) for word in words]  

print("orginal words:", words)
print("Stemmed words:", stem_word)
print("Lemmatized words:", lemm_word) # Lemmatization