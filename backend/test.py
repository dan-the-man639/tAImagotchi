from pet import Pet
from vital import *
import random
import json


pet = Pet.create_from_state("pet_state.json")

with open("activities.json", "r") as file:
    data = json.load(file)

activities = data["activities"]
while True:
    new_activity = pet.get_activities()
    print(new_activity)
    activities.extend(new_activity)
    with open("activities.json", 'w') as file:
        json.dump(data, file, indent=4)
    