from dotenv import load_dotenv
import os
from fastapi import FastAPI
import cohere


COHERE_KEY = os.getenv('COHERE')

co = cohere.Client(COHERE_KEY)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
