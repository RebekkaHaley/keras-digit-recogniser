"""Train a Keras NN model to predict digits.
"""

import logging
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.utils.np_utils import to_categorical

root = Path(__file__).parent.parent
model_filename = root / 'data/model.pkl'
train_filename = root / 'data/train.csv'

logger = logging.getLogger('train_model')

# Load data sets
train = pd.read_csv(train_filename)

# Organise data sets
X_train = train.iloc[:,1:].values.astype('float32')  # drop header row
y_train = train.iloc[:,0].values.astype('int32')  # keep labels only

# Normalize pixel values
X_train_norm = X_train / 255

# One Hot encoding labels
y_train_ohe = to_categorical(y_train)
num_classes = y_train_ohe.shape[1]

# Fix random seed for reproducibility
seed = 43
np.random.seed(seed)

# Design neural network architecture
model = Sequential()
model.add(Dense(64, activation='relu',input_dim=(28 * 28)))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.15))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.15))
model.add(Dense(10, activation='softmax'))

# Compile network
model.compile(
    optimizer=RMSprop(learning_rate=0.001),  # optimizer to update network and reduce loss value
    loss='categorical_crossentropy',  # loss function to measure efficacy of network
    metrics=['accuracy'])  # metrics to monitor performance of network

# Run
history = model.fit(X_train_norm, y_train_ohe, validation_split=0.05, epochs=15, batch_size=64)
logger.info('Model has finished training.')

# Save to disk
pickle.dump(model, open(model_filename, 'wb'))
logger.info(f'Model has been saved to: {model_filename}.')
