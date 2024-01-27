import os
from fastapi import FastAPI
from routes import router as extra_router
from shared import game, pet, counter  # Import game from the shared module

import cohere
from pet import Pet
from game import Game
import asyncio


from contextlib import asynccontextmanager

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
app.include_router(extra_router)

@app.get("/")
async def read_root():
    return {"Hello": str(counter)}
