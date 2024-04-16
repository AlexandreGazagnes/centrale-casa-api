"""
Main application file 
"""

from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.get("/predict/{description}")
async def predict(description):

    # all possible labels
    categ_list = ["watches", "baby care", "home furniture"]

    # best prediction system of the world
    predicted_value = random.choice(categ_list)

    return {"category": predicted_value, "description": description}
