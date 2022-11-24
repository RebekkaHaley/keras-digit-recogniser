"""Predict digit(s) using trained Keras NN model.
"""

import logging
import pickle
from pathlib import Path

import numpy as np
import pandas as pd

root = Path(__file__).parent.parent
model_filename = root / 'app/model.pkl'
input_filename = root / 'data/test.csv'
result_filename = root / 'data/result.csv'

logger = logging.getLogger('predict')

# Load the model from disk
loaded_model = pickle.load(open(model_filename, 'rb'))
input = pd.read_csv(input_filename)

# Run prediction
prediction = loaded_model.predict(input, verbose=0)

# Save to disk
df = pd.DataFrame({'classes': np.argmax(prediction, axis=1)})
df.to_csv(result_filename)
logger.info(f'Predicted classes have been saved to: {result_filename}.')
