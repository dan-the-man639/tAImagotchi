import json
from vital import Vital
import cohere
import os
from dotenv import load_dotenv
import numpy as np
import random
from embed import calculate_proj_len

load_dotenv()

COHERE_KEY = os.getenv('COHERE')
co = cohere.Client(COHERE_KEY)

END_SEQUENCES = ["How", "There", "Would"]
ACTIVITIES_PROMPT = '{"activities": ["Eat McDonald\'s", "Listen to NSYNC", "Watch Back to the Future", "Go to McDonald\'s Play Palace"]} Change to some other nostalgic activities in the 1990s and early 2000s and only output json. Only resond with json.'

BANNED_PHRASES = ["language", "model", "cohere", "request", "sure"]

with open("food_activities.json", "r") as file:
    data = json.load(file)
    FOOD_ACTIVITIES = data["food_activities"]

SATIATION_AVG_PROJ = 0.20262
ENERGY_AVG_PROJ = 0.20349
HAPPINESS_AVG_PROJ = 0.23083
INTELLECT_AVG_PROJ = 0.17589

AVG_PROJ_LENS = [SATIATION_AVG_PROJ, ENERGY_AVG_PROJ, HAPPINESS_AVG_PROJ, INTELLECT_AVG_PROJ]

VITAL_DEFAULT_CHANGE_RATE = -1

class Pet:
    def __init__(self, name: str, is_alive: bool, age: int, emotion: int, vitals: list, chat_history: list):
        self.name = name
        self.is_alive = is_alive
        self.age = age # days
        self.emotion = emotion
        self.vitals = [Vital.create_from_dict(vital_dict) for vital_dict in vitals]
        self.chat_history = chat_history
        self.vital_change_rate = VITAL_DEFAULT_CHANGE_RATE
    
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
            "emotion": self.emotion,
            "vitals": [vital.to_dict() for vital in self.vitals],
            "vital_change_rate": self.vital_change_rate
        }

    def dump_state(self, json_path):
        json_data = json.dumps(self.to_dict(), indent=4)
        with open(json_path, 'w') as file:
            file.write(json_data)
    
    def print_state(self):
        print(self.to_dict())

    
    def get_vitals(self):
        return self.vitals

    def get_random_complaint(self):
        complaint_prompts = []
        for vital in self.vitals:
            complaint_prompts.append(vital.get_complaint_prompt())
        random_complaint = np.random.choice(complaint_prompts)
        while True:
            print('generating dialogue')
            try_again = False
            responses = co.generate(prompt=random_complaint, temperature=0.9, end_sequences=END_SEQUENCES)
            for response in responses:
                do_next = False
                response_text = response.text
                start_quote_idx = response_text.find("\"")
                response_text = response_text[start_quote_idx + 1:]
                end_quote_idx = response_text.find("\"")
                response_text = response_text[:end_quote_idx]
                
                lower_case_response = response_text.lower()
                if len(response_text) > 160:
                    do_next = True
                for phrase in BANNED_PHRASES:
                    if phrase in lower_case_response:
                        do_next = True
                if not do_next:
                    try_again = False
                    break
            if try_again:
                continue
            else:
                break
        # print(random_complaint)
        return response_text
    
    def change_random_vitals(self):
        depression_factor = self.vitals[2].get_bin()
        for vital in self.vitals:
            if (vital.get_type_name() != "Energy"):
                print("change: ",depression_factor // 2)
                vital.set_change_rate(VITAL_DEFAULT_CHANGE_RATE - depression_factor // 2)
            print(vital.change_rate)
            vital.change_random()
    
    def get_activities(self) -> list:
        if self.vitals[1].get_bin() == 0:
            return []
        elif self.vitals[1].get_bin() == 1 and random.random() < 0.5:
            return []
        elif self.vitals[1].get_bin() == 2 and random.random() < 0.2:
            return []
            
        message = "generate another, only give the json" if self.chat_history else ACTIVITIES_PROMPT
        try_again = True
        while try_again:
            try:
                response = co.chat(message=message, chat_history=self.chat_history, temperature=0.9)
                edited_text = response.text.replace("```", "").replace("json", "")
                json_dict = json.loads(edited_text)
                try_again = False
                activities = [activity for activity in json_dict["activities"]]
                while len(activities) < 4:
                    activities.append(FOOD_ACTIVITIES[random.randint(0, len(FOOD_ACTIVITIES) - 1)])
                while len(activities) > 4:
                    activities.pop()
            except:
                try_again = True
        self.chat_history.append({"role": "USER", "text": message})
        self.chat_history.append({"role": "CHATBOT", "text": edited_text})
        
        
        if random.random() < 0.4:
            activities[random.randint(0, len(activities) - 1)] = FOOD_ACTIVITIES[random.randint(0, len(FOOD_ACTIVITIES) - 1)]
        return activities
    
    def handle_activity(self, activity: str) -> None:
        activity_proj_lens = calculate_proj_len(activity)
        for idx, vital in enumerate(self.vitals):
            over = activity_proj_lens[idx] - AVG_PROJ_LENS[idx]
            if over > 0 and vital.get_type_name() == "Energy":
                vital.set_value(vital.get_value() - over * 50)
            elif over > 0 and vital.get_type_name() == "Satiation":
                vital.set_value(vital.get_value() + over * 200)
            elif ("play" in activity.lower() or "watch" in activity.lower()) and vital.get_type_name() == "Happiness":
                vital.set_value(vital.get_value() + 40)
            elif "listen" in activity.lower() and vital.get_type_name() == "Intellect":
                vital.set_value(vital.get_value() + 40)
            elif vital.get_type_name() == "Energy":
                vital.set_value(vital.get_value() - 10)
            elif over > 0:
                vital.set_value(vital.get_value() + over * 100)
            
