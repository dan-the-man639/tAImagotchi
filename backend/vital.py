
'''
vital bins: zero, very low, low, high, full
'''

BASE_PROMPT = "You are a cute tamagotchi pet. In your short response, do not mention that you are a language model. "


class Vital:
    def __init__(self, value: int, bins: list):
        self.type_name = type(self).__name__
        self.value = value
        self.bins = bins
    
    @staticmethod
    def create_from_dict(vital_dict: dict) -> 'Vital':
        type_name = vital_dict["type_name"]
        vital_dict.pop("type_name")
        if type_name == "Satiation":
            return Satiation(**vital_dict)
         
    
    def to_dict(self) -> dict:
        return {
            "type_name": self.type_name,
            "value": self.value,
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

class Satiation(Vital):
    def __init__(self, value: int, bins: list):
        super().__init__(value, bins)
        self.complaint_prompts = [
            "Say something that shows how hungry you are and that you might starve soon.",
            "Say something that shows that you are very hungry.",
            "Say something that shows you are kind of hungry.",
            "Say something that shows that you feel satiated.",
            "Say something that shows that you are extremely full and don't want to eat."
        ]
        
