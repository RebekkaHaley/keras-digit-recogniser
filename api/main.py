"""todo.
"""

from fastapi import FastAPI

app = FastAPI()

# Handle GET request
@app.get('/')
async def prediction_endpoint():
    return {"hello": "world"}

# Handle POST request
