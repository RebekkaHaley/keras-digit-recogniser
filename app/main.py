"""todo.
"""

import base64
import pickle
from pathlib import Path

import numpy as np
from cv2 import (COLOR_BGR2GRAY, IMREAD_COLOR, INTER_LINEAR, cvtColor,
                 imdecode, resize)
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Load prebuilt model
model_filename = Path.cwd() / 'model.pkl'
model = pickle.load(open(model_filename, 'rb'))

# Initialize app
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Handle GET request
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Handle POST request
@app.post("/")
def canvas(request: Request):

    # Recieve base64 data from the user form
    canvasdata = request.form['canvasimg']
    encoded_data = request.form['canvasimg'].split(',')[1]

    # Decode base64 image to python array
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = imdecode(nparr, IMREAD_COLOR)

    # Convert 3 channel image (RGB) to 1 channel image (GRAY)
    gray_image = cvtColor(img, COLOR_BGR2GRAY)

    # Resize to (28, 28)
    gray_image = resize(gray_image, (28, 28), interpolation=INTER_LINEAR)

    # Expand to numpy array dimenstion to (1, 28, 28)
    img = np.expand_dims(gray_image, axis=0)

    try:
        prediction = np.argmax(model.predict(img))
        print(f"Prediction Result : {str(prediction)}")
        return templates.TemplateResponse(
            "drawing.html",
            context={
                "request": request,
                "response": str(prediction),
                "canvasdata": canvasdata,
                "success": True})
    except Exception as e:
        return templates.TemplateResponse(
            "drawing.html",
            context={
                "request": request,
                "response": str(e),
                "canvasdata": canvasdata})
