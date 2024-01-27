import json
from vital import Vital
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

COHERE_KEY = os.getenv('COHERE')
co = cohere.Client(COHERE_KEY)

STOP_SEQUENCES = ["\n"]

class Pet:
    def __init__(self, name: str, is_alive: bool, age: int, vitals: list):
        self.name = name
        self.is_alive = is_alive
        self.age = age # days
        self.vitals = [Vital.create_from_dict(vital_dict) for vital_dict in vitals]
    
    @staticmethod
    def create_from_state(json_path: str) -> 'Pet':
        with open(json_path, 'r') as file:
            json_dict = json.load(file)
        return Pet(**json_dict)
    
    def to_dict(self):
        return {
            "name": self.name,
            "is_alive": self.is_alive,
            "age": self.age,
            "vitals": [vital.to_dict() for vital in self.vitals]
        }

    def dump_state(self, json_path):
        json_data = json.dumps(self.to_dict(), indent=4)
        with open(json_path, 'w') as file:
            file.write(json_data)
    
    def print_state(self):
        print(self.to_dict())

    def show(self):
        print(f"I am {self.name} and I am {self.age} days old.")
    
    def get_vitals(self):
        return self.vitals

    def get_complaints(self):
        complaints = []
        for vital in self.vitals:
            complaint_prompt = vital.get_complaint_prompt()
            response = co.generate(prompt=complaint_prompt, temperature=0.9, stop_sequences=STOP_SEQUENCES)
            complaints.append(response[0].text)
        return complaints
    
    def decrease_random_vitals(self):
        for vital in self.vitals:
            vital.decrease_random()

