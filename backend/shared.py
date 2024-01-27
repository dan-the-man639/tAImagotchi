# shared.py
from pet import Pet
from game import Game

pet = Pet.create_from_state("pet_state.json")
game = Game(pet)
counter = 0
