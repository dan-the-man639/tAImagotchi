from pet import Pet


class Game:
    def __init__(self):
        self.is_running = True
    
    def reset(self):
        self.pet = Pet.create_from_state("pet_state.json")
    
    def start(self):
        self.reset()
        self.is_running = True
        
    
    def stop(self):
        self.is_running = False
    
    def update(self):
        self.pet.decrease_random_vitals()
    
    def get_pet_state(self):
        return self.pet.to_dict()
    
    def get_random_complaint(self):
        return self.pet.get_random_complaint()
    
    def get_activities(self):
        return self.pet.get_activities()
    
    