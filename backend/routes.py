# routes.py
from fastapi import APIRouter
from pydantic import BaseModel
from shared import game  # Import game from the shared module

router = APIRouter()

@router.get("/reset-stats")
async def reset_stats():
    game.reset()
    return "Game has been reset"

@router.get("/get-stats")
async def get_stats():
    stats = game.get_pet_state()
    vitals = stats["vitals"]
    vital_stats = [{"Type": vital["type_name"], "Stat": vital["value"]} for vital in vitals]
    return vital_stats

@router.get("/get-state")
async def get_state():
    stats = game.get_pet_state()
    vital_stats = {"is_alive": stats["is_alive"], "emotion": stats["emotion"]}
    return vital_stats

@router.get("/generate-trigger")
async def generate_trigger():
    return game.get_random_complaint()

@router.get("/generate-options")
async def generate_options():
    options =  game.get_activities()
    print(options)
    return options


class ActionRequest(BaseModel):
    action: str

@router.post("/handle-action")
async def handle_action(request: ActionRequest):
    action_string = request.action
    game.handle_activity(action_string)
    return {"message": "Action received"}
