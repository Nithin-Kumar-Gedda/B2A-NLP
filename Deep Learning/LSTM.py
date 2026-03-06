import numpy as np
import tensorflow as tf # pyright: ignore[reportMissingImports]
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, SpatialDropout1D

#ensure reproducibility
np.random.seed(42)
tf.random.set_seed(42)

sentences = [
    "I really love this product; it works perfectly.",
    "The meeting is scheduled for tomorrow morning.",
    "The movie was amazing and I enjoyed every moment.",
    "The food tasted terrible and was cold.",
    "The customer service was very helpful and friendly.",
    "The application keeps crashing and it is frustrating.",
    "This restaurant serves delicious food and the atmosphere is wonderful.",
    "I am extremely satisfied with the quality of this laptop.",
    "I regret buying this product because it stopped working.",
    "I am very disappointed with this service.",
    "I bought a new phone last week.",
    "The hotel room was dirty and uncomfortable.",
]

labels =[1,0.5,1,0,1,0,1,1,0,0,0.5,0]

max_words = 10000
max_len = 50

tokenizer = Tokenizer(num_words = max_words, oov_token = "<OOV>")
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)
padded_sequences = pad_sequences(sequences, maxlen=max_len, padding = 'post')

# convert into num array
labels = np.array(labels)

# model LSTM
model = Sequential([
    Embedding(max_words, 128, input_length = max_len),
    SpatialDropout1D(0.2),
    LSTM(100, dropout=0.2, recurrent_dropout=0.2),
    Dense(1,activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

model.fit(padded_sequences, labels, epochs=5, batch_size=2,verbose=1)

# function to predict sentiment
def predict_sentiment(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len, padding='post')

    prediction =model.predict(padded)

    if prediction >0.5:
        return "Positive"
    elif prediction<0.5:
        return "Negative"
    else:
        return "Neutral"


# Testing
text_sentence = input("Enter Sentence: ")
print(f"Sentence: {text_sentence}")
print(f"Sentiment: {predict_sentiment(text_sentence)}")
