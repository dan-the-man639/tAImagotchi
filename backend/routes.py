# routes.py
from fastapi import APIRouter
from shared import game  # Import game from the shared module

router = APIRouter()

@router.get("/reset-stats")
async def reset_stats():
    return "Reset stats"

@router.get("/get-stats")
async def get_stats():
    stats = game.get_pet_state()
    vitals = stats["vitals"]
    vital_stats = {vital["type_name"]: vital["value"] for vital in vitals}
    return vital_stats

@router.get("/generate-trigger")
async def generate_trigger():
    return "Generated trigger"

@router.get("/handle-action")
async def handle_action():
    return "Handled action"
