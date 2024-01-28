import numpy as np

'''
vital bins: zero, very low, low, high, full
'''

VITAL_DECREASE_STDEV = 2

BASE_PROMPT = "There is a cute pet that"
END_PROMPT = "What would that pet say? Give the short direct response and don't mention being a language model"

class Vital:
    def __init__(self, value: int, change_rate: int, bins: list):
        self.type_name = type(self).__name__
        self.change_rate = change_rate # per game cycle
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
        else:
            return Intellect(**vital_dict)
         
    
    def to_dict(self) -> dict:
        return {
            "type_name": self.type_name,
            "value": self.value,
            "change_rate": self.change_rate,
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
        return BASE_PROMPT + self.complaint_prompts[self.get_bin()] + END_PROMPT
    
    def random_change(self) -> None:
        change_amount = np.random.normal(self.change_rate, VITAL_DECREASE_STDEV)
        raw_value = np.floor(self.value + change_amount)
        raw_value = max(raw_value, 0)
        raw_value = min(raw_value, 100)
        self.value = raw_value

class Satiation(Vital):
    def __init__(self, value: int, change_rate: int, bins: list):
        super().__init__(value, change_rate, bins)
        self.complaint_prompts = [
            "is about to starve to death.",
            "is hungry in a negative way.",
            "is mildly hungry.",
            "feels very full but in a positive way."
        ]

class Energy(Vital):
    def __init__(self, value: int, change_rate: int, bins: list):
        super().__init__(value, change_rate, bins)
        self.complaint_prompts = [
            "is going to collapse and fall asleep any minute.",
            "is tired.",
            "feels moderately awake.",
            "feels extremely full of energy."
        ]

class Happiness(Vital):
    def __init__(self, value: int, change_rate: int, bins: list):
        super().__init__(value, change_rate, bins)
        self.complaint_prompts = [
            "feels extremely depressed.",
            "feels kind of sad.",
            "feels moderately happy and content.",
            "feels beyond happy and joyful and love life."
        ]

class Intellect(Vital):
    def __init__(self, value: int, change_rate: int, bins: list):
        super().__init__(value, change_rate, bins)
        self.complaint_prompts = [
            "is extremely dumb.",
            "is kind of dumb.",
            "is reasonably smart.",
            "is a genius"
        ]

    

