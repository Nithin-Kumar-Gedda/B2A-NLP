import nltk
from nltk.corpus import wordnet

polysemy_words = ['bank', 'bat', 'book']
print("Polysemy:")
for word in polysemy_words:
    synsets = wordnet.synsets(word)
    print(f"{word}:{len(synsets)} senses")

homonymy_words = ['bat','can','fair']
print("\nHomonymy:")
for word in homonymy_words:
    synsets = wordnet.synsets(word)
    print(f"{word}:{len(synsets)} meanings")

polysemy_word = 'bank'
homonymy_word = 'bat'

# print(f"\nDefinition for '{polysemy_word}':")
# for synset in wordnet.synsets(polysemy_word):
#     # print(f"{synset.name()}: {synset.definition()}")

# Homonymys

# # print(f"\nDefinition for '{homonymy_word}':")
# for synset in wordnet.synsets(homonymy_word):
#     # print(f"{synset.name()}: {synset.definition()}")

#Hypernyms

# syn = wordnet.synsets('apple')[0]
# hypernyms = syn.hypernyms()
# print("Hypernyms of 'apple': ", hypernyms)

# Hyponyms

# syn = wordnet.synsets('fruit')[0]
# hyponyms = syn.hyponyms()
# print("Hypernyms of 'apple': ", hyponyms)

word = "good"

synonyms = []
for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

synonyms = list(set(synonyms))
print(f"'{word}' : {synonyms} ")

antonyms = []
for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())

antonyms = list(set(antonyms))
print(f"'{word}' : {antonyms}")


