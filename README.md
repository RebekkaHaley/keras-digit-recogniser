## Welcome

This repo contains code for using ML to recognise digits from 280x280 images.

## Setup

After downloading the repo, follow these instructions:

1) `poetry install`.

2) `cd app`.

3) `poetry run uvicorn main:app --reload`.

4) Go to `localhost:8000` in browser.

## App

The folder `/app` contains source code for the FastAPI app that allows users to draw and predict digits.

## Model Logic

The folder `/model_logic` contains code for creating a submission to the Kaggle competition "Digit Recognizer", and used Keras NN to predict the class of number for a given test data point.

The resulting submission scored approx. 0.97/1.

## Accessing the original data set

Please note that the train and test CSV files have not been included due to large file size. These files can instead be accessed on the Kaggle website at: [Digit Recognizer/Data](https://www.kaggle.com/competitions/digit-recognizer/data).

## Resources

- [Lets create a Drawing APP with JS](https://dev.to/0shuvo0/lets-create-a-drawing-app-with-js-4ej3)
- [How To Deploy Digit Recognition Model Into Drawing App](https://medium.com/analytics-vidhya/how-to-deploy-digit-recognition-model-into-drawing-app-6e59f82a199c)
