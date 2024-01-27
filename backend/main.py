import os
from fastapi import FastAPI
import cohere
from pet import Pet
from game import Game
import asyncio


from contextlib import asynccontextmanager

pet = Pet.create_from_state("pet_state.json")
game = Game(pet)
counter = 0

@asynccontextmanager
async def lifespan(app: FastAPI):
    global counter
    # Startup logic: Starting the game loop
    task = asyncio.create_task(run_game())
    yield
    # Shutdown logic: Stopping the game loop
    task.cancel()

async def run_game():
    global counter
    while game.is_running:
        game.update()
        pet.print_state()
        await asyncio.sleep(1) # seconds per game cycle

def get_game():
    return game

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello": str(counter)}
        
@app.get("/get-stats")
async def getStats():
    return {"Stats": game()}
