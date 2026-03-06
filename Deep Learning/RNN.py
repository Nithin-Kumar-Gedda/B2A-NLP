import numpy as np
import tensorflow as tf 
np.random.seed(0)
seq_length = 10 
data = np.random.randn(100, seq_length)

x = data[:, :-1]
y = data[:, 1:]

# define RNN model
model = tf.keras.Sequential([
    tf.keras.layers.SimpleRNN(10, input_shape=(None, seq_length-1)),
    tf.keras.layers.Dense(seq_length-1)
])

# compile model
model.compile(loss='mse', optimizer= 'adam')

#Train model
model.fit(x[:, np.newaxis, :],y, epochs=20, batch_size=32)

# Generate predictions
predictions = model.predict(x[:, np.newaxis, :])

print("Sample Predictions:")
for i in range(1):
    print("Input:",x[i])
    print("Target:",y[i])
    print("Prediction:", predictions[i])
    print()
