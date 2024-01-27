from dotenv import load_dotenv
import os
from fastapi import FastAPI
import cohere
from pet import Pet
from game import Game


COHERE_KEY = os.getenv('COHERE')
co = cohere.Client(COHERE_KEY)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}



async def start_game():
    pet = Pet.create_from_state("pet_state.json")
    game = Game(pet)
    while game.is_running:
        # game logic
        game.update()
        
        
        
