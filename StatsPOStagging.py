import nltk
from nltk.corpus import treebank, brown
from nltk.classify import MaxentClassifier

from nltk.tag import BrillTaggerTrainer
from nltk.tag import DefaultTagger

nltk.download('punkt')
nltk.download('treebank')
nltk.download('brown')

# Hidden Markov Model(HMM) POS Tagging 

train_data = treebank.tagged_sents()[:3000] # using first 3000 sentences for training.
hmm_tagger = nltk.HiddenMarkovModelTagger.train(train_data)

sentence = "We are talking about POS Tagging in this chapter."
tokens = nltk.word_tokenize(sentence)

tags = hmm_tagger.tag(tokens)
# print(tags)

# Maximum Entropy (MaxEnt)

brown_sents = brown.tagged_sents()  #loads tagged sentences from the Brown corpus

brown_sents_subset = brown_sents[:int(len(brown_sents))]

#feature extraction

def features(sentence, i):
    word = sentence[i][0]
    pos = sentence[i][1]
    features = {
        'word' : word.lower(),
        'is_first': i == 0,
        'is_last': i == len(sentence)-1,
        'prev_tag': sentence[i-1][1] if i>0 else 'None',
        'next_tag': sentence[i+1][1] if i<len(sentence)-1 else 'None' 
    }
    return features

train_features = [(features(s, i), tag) for s in brown_sents_subset for i, (word, tag) in enumerate(s)]

classifier = MaxentClassifier.train(train_features)

test_sentence = ["the", "quick", "brown", "fox"]

test_features = [features(test_sentence, i) for i, word in enumerate(test_sentence)]

tags = classifier.classify_many(test_features)
print(list(zip(test_sentence, tags)))

# Rule-based transformational Tagger

training_data = treebank.tagged_sents()[:50000]
test_data = treebank.tagged_sents()[50000:55000]

default_tagger = DefaultTagger('NN')

temp = nltk.tag.brill.brill24()
brill_trainer = BrillTaggerTrainer(default_tagger, temp)
brill_tagger = brill_trainer.train(training_data, max_rules=10)

accuracy = brill_tagger.evaluate(test_data)
print(f"Brill Tagger Accuracy: {accuracy:.4f}")

sentence = "This is simple sentence"
tokens = nltk.word_tokenize(sentence)
tagged_sentence = brill_trainer.tag(tokens)
print(tagged_sentence)