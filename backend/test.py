from pet import Pet
from game import Game
from vital import *
import random
import json


game = Game()
game.reset()
print(game.get_pet_state())
game.get_random_complaint()
game.handle_activity("Watch a movie")
print(game.get_pet_state())