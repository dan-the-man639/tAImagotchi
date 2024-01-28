import os
from fastapi import FastAPI
from routes import router as extra_router
from shared import game, counter  # Import game from the shared module

import cohere
from pet import Pet
from game import Game
import asyncio
from fastapi.middleware.cors import CORSMiddleware


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
    game.start()
    while game.is_running:
        game.update()
        await asyncio.sleep(5) # seconds per game cycle

def get_game():
    return game

app = FastAPI(lifespan=lifespan)
# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
app.include_router(extra_router)

@app.get("/")
async def read_root():
    return {"Hello": str(counter)}
