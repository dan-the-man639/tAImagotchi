import numpy as np

'''
vital bins: zero, very low, low, high, full
'''

VITAL_DECREASE_STDEV = 2

BASE_PROMPT = "You are a cute tamagotchi pet. In your short response, do not mention that you are a language model and do not respond to the player. Say something that shows that"


class Vital:
    def __init__(self, value: int, decrease_rate: int, bins: list):
        self.type_name = type(self).__name__
        self.decrease_rate = decrease_rate # per game cycle
        self.value = value
        self.bins = bins
        self.complaint_prompts = []
    
    @staticmethod
    def create_from_dict(vital_dict: dict) -> 'Vital':
        type_name = vital_dict["type_name"]
        vital_dict.pop("type_name")
        if type_name == "Satiation":
            return Satiation(**vital_dict)
        elif type_name == "Energy":
            return Energy(**vital_dict)
        elif type_name == "Happiness":
            return Happiness(**vital_dict)
         
    
    def to_dict(self) -> dict:
        return {
            "type_name": self.type_name,
            "value": self.value,
            "decrease_rate": self.decrease_rate,
            "bins": self.bins
        }
    
    def get_value(self) -> int:
        return self.value
    
    def set_value(self, value: int) -> None:
        self.value = value
    
    def get_bin(self) -> int:
        for idx, bin in enumerate(self.bins):
            if self.value <= bin:
                return idx
    
    def get_complaint_prompt(self) -> str:
        return BASE_PROMPT + self.complaint_prompts[self.get_bin()]
    
    def decrease_random(self) -> None:
        decrease_amount = np.random.normal(self.decrease_rate, VITAL_DECREASE_STDEV)
        self.value = max(0, np.floor(self.value - decrease_amount))

class Satiation(Vital):
    def __init__(self, value: int, decrease_rate: int, bins: list):
        super().__init__(value, decrease_rate, bins)
        self.complaint_prompts = [
            "Say something that shows that you starved to death.",
            "Say something that shows how hungry you are and that you might starve soon.",
            "Say something that shows you are kind of hungry.",
            "Say something that shows that you feel satiated.",
            "Say something that shows that you are extremely full and don't want to eat."
        ]

class Energy(Vital):
    def __init__(self, value: int, decrease_rate: int, bins: list):
        super().__init__(value, decrease_rate, bins)
        self.complaint_prompts = [
            "Say something that shows that you have fallen into deep slumber",
            "Say something that shows that you are going to fall asleep any minute.",
            "Say something that shows that you are really tired.",
            "Say something that shows that you feel awake.",
            "Say something that shows that you are full of engery."
        ]

class Happiness(Vital):
    def __init__(self, value: int, decrease_rate: int, bins: list):
        super().__init__(value, decrease_rate, bins)
        self.complaint_prompts = [
            "Say something that shows that you are extremely depressed.",
            "Say something that shows that you are kind of sad.",
            "Say something that shows that you are kind of happy.",
            "Say something that shows that you are really happy.",
            "Say something that shows that you are beyond happy."
        ]

class 

    

