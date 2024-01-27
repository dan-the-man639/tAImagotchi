import json
from vital import Vital
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

COHERE_KEY = os.getenv('COHERE')
co = cohere.Client(COHERE_KEY)

STOP_SEQUENCES = ["\n"]
ACTIVITIES_PROMPT = '{"activities": ["Eat cake", "Listen to NSYNC", "Watch Back to the Future", "Go to McDonald\'s Play Palace"]} Change the activities to ones popular in the 1990s and early 2000s and only output the json. Only resond with json'

class Pet:
    def __init__(self, name: str, is_alive: bool, age: int, vitals: list, chat_history: list):
        self.name = name
        self.is_alive = is_alive
        self.age = age # days
        self.vitals = [Vital.create_from_dict(vital_dict) for vital_dict in vitals]
        chat_history = chat_history
    
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

    def get_random_complaint(self):
        complaint_prompts = []
        for vital in self.vitals:
            complaint_prompts.append(vital.get_complaint_prompt())
        random_complaint = np.random.choice(complaint_prompts)
        response = co.generate(prompt=random_complaint, temperature=0.9, stop_sequences=STOP_SEQUENCES)
        return response[0].text
    
    def decrease_random_vitals(self):
        for vital in self.vitals:
            vital.decrease_random()
    
    def get_activities(self):
        message = ACTIVITIES_PROMPT if self.chat_history.empty() else "generate anthother"
        response = co.chat(message=message)
        self.chat_history.append({"role": "USER", "text": message})
        self.chat_history.append({"role": "CHATPOT", "text": response[0].text})
        json_dict = json.loads(response[0].text)
        for activity in json_dict["activities"]:
            print(activity)
