## Welcome

This repo contains a FastAPI app that allows users to draw and predict digits using a Keras Convolutional Neural Network (CNN).

## Setup

If running app with pipenv:

1) `pipenv install`.

2) `pipenv run uvicorn app.main:app --reload`.

3) Go to `localhost:8000` in browser.

If running app with docker:

1) `docker build -t keras-digit-recogniser .`.

2) `docker run -p 80:80 keras-digit-recogniser`.

3) Go to `localhost` in browser.

## App

The folder `/app` contains the source code.

## Model Logic

The folder `/model_logic` contains the notebook used to create the CNN model. It also produces a CSV in the correct submission format for the Kaggle competition "Digit Recognizer".

For example, one submission scored approx. 0.97.

## Accessing the original data set

Please note that the train and test CSV files have not been included due to large file size. These files can instead be accessed on the Kaggle website at: [Digit Recognizer/Data](https://www.kaggle.com/competitions/digit-recognizer/data).

## Resources

- [Lets create a Drawing APP with JS](https://dev.to/0shuvo0/lets-create-a-drawing-app-with-js-4ej3)
- [How To Deploy Digit Recognition Model Into Drawing App](https://medium.com/analytics-vidhya/how-to-deploy-digit-recognition-model-into-drawing-app-6e59f82a199c)
- [Deploy ML models with FastAPI, Docker, and Heroku](https://www.youtube.com/watch?v=h5wLuVDr0oc&list=WL&index=3)
- [Jinja2 Templates with FastAPI for Python](https://www.youtube.com/watch?v=IxXtDOI9RUo)
- [Dockerizing Python Poetry Applications](https://medium.com/@harpalsahota/dockerizing-python-poetry-applications-1aa3acb76287)
- [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)
- [Mouse cursor doesn't match with canvas](https://stackoverflow.com/questions/30082590/mouse-cursor-doesnt-match-with-canvas)