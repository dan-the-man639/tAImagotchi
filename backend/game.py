from pet import Pet


class Game:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.is_running = True
    
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def update(self):
        self.pet.decrease_random_vitals()
    
    
    