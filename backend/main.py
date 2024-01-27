import os
from fastapi import FastAPI
import cohere
from pet import Pet
from game import Game
import asyncio


app = FastAPI()
pet = Pet.create_from_state("pet_state.json")
game = Game(pet)

@app.get("/")
async def read_root():
    return {"Hello": "World"}



async def start_game():
    while game.is_running:
        # game logic
        game.update()
        await asyncio.sleep(1)
        
        
        
        
