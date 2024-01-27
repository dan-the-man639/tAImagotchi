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
    
    def get_pet_state(self):
        return self.pet.to_dict()
    
    def get_random_complaint(self):
        return self.pet.get_random_complaint()
    
    def get_activities(self):
        return self.pet.get_activities()
    
    