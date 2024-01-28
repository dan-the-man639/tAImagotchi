from pet import Pet
from game import Game
from vital import *
import random
import json


game = Game()
game.reset()
while True:
    game.get_activities()
    