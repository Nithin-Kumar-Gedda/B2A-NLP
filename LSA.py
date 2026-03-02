import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer

docs = [
    "The thief robbed a place.",
    "The police chased the thief.",
    "The police could not catch the thief.",
    "The thief robbed another place the next day."
]

vectorizer = CountVectorizer()  #Victorize the Docs
X = vectorizer.fit_transform(docs)

svd = TruncatedSVD(n_components=2) #Singular Value Decomposition & #LSA(latent semantic analysis)
X_reduced = svd.fit_transform(X)

terms = vectorizer.get_feature_names_out()
components = svd.components_

print("Original Term-Document Matrix: \n", X.toarray())
print("Reduced Term-Document Matrix: \n", X_reduced)
print("Terms:\n", terms)
print("Components:\n", components)
