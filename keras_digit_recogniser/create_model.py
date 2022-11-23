"""
"""

# Imports
import numpy as np
import pandas as pd
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense , Dropout
from keras.optimizers import RMSprop

# Load data sets
train = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')

# Organise data sets
X_train = train.iloc[:,1:].values.astype('float32')  # drop header row
y_train = train.iloc[:,0].values.astype('int32')  # keep labels only
X_test = test.values.astype('float32')

# Reshape image in 3 dimensions, i.e., (num_images, img_rows, img_cols)
X_train_3d = X_train.reshape(X_train.shape[0], 28, 28)

# Normalize pixel values
X_train_norm = X_train / 255
X_test_norm = X_test / 255

# One Hot encoding labels
y_train_ohe = to_categorical(y_train)
num_classes = y_train_ohe.shape[1]

# Fix random seed for reproducibility
seed = 43
np.random.seed(seed)

# Design neural network architecture
model = Sequential()
model.add(Dense(32,activation='relu',input_dim=(28 * 28)))
model.add(Dense(16,activation='relu'))
model.add(Dense(10,activation='softmax'))

# Compile network
model.compile(
    optimizer=RMSprop(learning_rate=0.001),  # optimizer to update network and reduce loss value
    loss='categorical_crossentropy',  # loss function to measure efficacy of network
    metrics=['accuracy'])  # metrics to monitor performance of network

# Run
history = model.fit(X_train_norm, y_train_ohe, validation_split=0.05, epochs=25, batch_size=64)

# Plot metrics
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
acc_values = history_dict['accuracy']
val_acc_values = history_dict['val_accuracy']
epochs = range(1, len(loss_values) + 1)

# We see that after the 15th epoch 'val_loss' is increasing and 'val_accuracy' is decreasing.
# This implies overfitting.
# To avoid this we will stop training after 15 epochs.


model = Sequential()
model.add(Dense(64, activation='relu',input_dim=(28 * 28)))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.15))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.15))
model.add(Dense(10, activation='softmax'))

model.compile(
    optimizer=RMSprop(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy'])

history = model.fit(X_train_norm, y_train_ohe, validation_split=0.05, epochs=15, batch_size=64)

# Plot metrics
history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
acc_values = history_dict['accuracy']
val_acc_values = history_dict['val_accuracy']
epochs = range(1, len(loss_values) + 1)

plt.plot(epochs, loss_values, 'bo', label='loss')  # blue dot
plt.plot(epochs, val_loss_values, 'b+', label='val_loss')  # blue crosses
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.show()
plt.clf()
plt.plot(epochs, acc_values, 'bo', label='accuracy')  # blue dot
plt.plot(epochs, val_acc_values, 'b+', label='val_accuracy')  # blue crosses
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

# Submission
predictions = model.predict(X_test_norm, verbose=0)
classes = np.argmax(predictions, axis=1)
submissions = pd.DataFrame({"ImageId": list(range(1, len(classes)+1)), "Label": classes})
