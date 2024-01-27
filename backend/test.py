from pet import Pet
from vital import *
import random


pet = Pet.create_from_state("pet_state.json")
pet.get_vitals()[0].set_value(random.randint(0, 100))
pet.print_state()
print(pet.get_complaints())