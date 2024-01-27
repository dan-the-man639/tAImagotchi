from pet import Pet
from vital import *
import random


pet = Pet.create_from_state("pet_state.json")

pet.print_state()
print(pet.get_complaints())