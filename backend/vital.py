import numpy as np

'''
vital bins: zero, very low, low, high, full
'''

VITAL_DECREASE_STDEV = 0.5

BASE_PROMPT = "Act as if you are a cute pet. Say something that shows"
END_PROMPT = "Wrap the quote in quotation marks. Do not say sure thing."

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
    
    def get_type_name(self) -> str:
        return self.type_name
    
    def get_value(self) -> int:
        return self.value
    
    def set_change_rate(self, change_rate: int) -> None:
        self.change_rate = change_rate
    
    def set_value(self, value: int) -> None:
        floored_value = min(100, max(0, np.floor(value)))
        self.value = floored_value
    
    def get_bin(self) -> int:
        for idx, bin in enumerate(self.bins):
            if self.value <= bin:
                return idx
    
    def get_complaint_prompt(self) -> str:
        return BASE_PROMPT + self.complaint_prompts[self.get_bin()] + END_PROMPT
    
    def change_random(self) -> None:
        change_amount = np.random.normal(self.change_rate, VITAL_DECREASE_STDEV)
        raw_value = np.floor(self.value + change_amount)
        raw_value = max(raw_value, 0)
        raw_value = min(raw_value, 100)
        self.value = raw_value

class Satiation(Vital):
    def __init__(self, value: int, change_rate: int, bins: list):
        super().__init__(value, change_rate, bins)
        self.complaint_prompts = [
            "that you are about to starve to death",
            "that you are really hungry.",
            "you are mildly hungry but okay for now.",
            "that you feel very full but in a positive way."
        ]

class Energy(Vital):
    def __init__(self, value: int, change_rate: int, bins: list):
        super().__init__(value, change_rate, bins)
        self.complaint_prompts = [
            "that you are going to fall asleep any second",
            "that you feel pretty tired.",
            "that you feel moderately awake.",
            "that you are extremely full of energy."
        ]
    def change_random(self) -> None:
        change_amount = np.random.normal(self.change_rate, VITAL_DECREASE_STDEV)
        raw_value = np.floor(self.value + change_amount + 4)
        raw_value = max(raw_value, 0)
        raw_value = min(raw_value, 100)
        self.value = raw_value

class Happiness(Vital):
    def __init__(self, value: int, change_rate: int, bins: list):
        super().__init__(value, change_rate, bins)
        self.complaint_prompts = [
            "that you are extremely depressed.",
            "that you are kind of sad.",
            "that you are reasonably happy and content.",
            "that you are beyond happy and joyful and love life."
        ]

class Intellect(Vital):
    def __init__(self, value: int, change_rate: int, bins: list):
        super().__init__(value, change_rate, bins)
        self.complaint_prompts = [
            "that you are extremely dumb, borderline moronic.",
            "that you are kind of dumb.",
            "that you are reasonably smart.",
            "how smart you feel without being boastful."
        ]

    

