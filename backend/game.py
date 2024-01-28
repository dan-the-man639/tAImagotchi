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
        for vital in self.pet.vitals:
            print(vital.get_type_name(), vital.value)
        print(self.pet.get_activities())
        if self.pet.vitals[0].value <= 0:
            self.pet.is_alive = False
            self.is_running = False
        self.pet.change_random_vitals()
        
    
    def get_pet_state(self):
        return self.pet.to_dict()
    
    def get_random_complaint(self):
        return self.pet.get_random_complaint()
    
    def get_activities(self):
        return self.pet.get_activities()
    
    def handle_activity(self, activity: str) -> None:
        return self.pet.handle_activity(activity)
    
    