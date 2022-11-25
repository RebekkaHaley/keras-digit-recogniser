"""Defines application routes.
"""

import base64
import pickle
from io import BytesIO
from pathlib import Path

import numpy as np
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from PIL import Image

# Initialize app
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Load ML model
model_filename = Path.cwd() / 'model.pkl'
model = pickle.load(open(model_filename, 'rb'))


# Models
class PredictionOut(BaseModel):
    digit: str


# Handle GET request
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# Handle POST request
@app.post("/", response_model=PredictionOut)
async def predict(uri=Form()):
    # Recieve base64 data from the user form
    image_data = uri.split(',')[1]

    # Decode base64 image to python array
    image_data = base64.b64decode(image_data)
    image_data = BytesIO(image_data)

    # Convert image from RGB to grayscale
    image = Image.open(image_data).convert("L").resize((28, 28))

    # Turn into an array of numbers
    image2arr = np.array(image)
    reshaped_image = image2arr.reshape(1, 28*28)

    # Run prediction
    digit = np.argmax(model.predict(reshaped_image))
    return {"digit": f"{digit}"}
