import json
from vital import Vital
import cohere
import os
from dotenv import load_dotenv
import numpy as np
import random

load_dotenv()

COHERE_KEY = os.getenv('COHERE')
co = cohere.Client(COHERE_KEY)

END_SEQUENCES = ["How", "There", "Would"]
ACTIVITIES_PROMPT = '{"activities": ["Eat cake", "Listen to NSYNC", "Watch Back to the Future", "Go to McDonald\'s Play Palace"]} Change to some other nostalgic activities in the 1990s and early 2000s and only output json. Only resond with json.'

BANNED_PHRASES = ["language", "model", "cohere", "request", "sure"]

class Pet:
    def __init__(self, name: str, is_alive: bool, age: int, emotion: int, vitals: list, chat_history: list):
        self.name = name
        self.is_alive = is_alive
        self.age = age # days
        self.emotion = emotion
        self.vitals = [Vital.create_from_dict(vital_dict) for vital_dict in vitals]
        self.chat_history = chat_history
    
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
            "vitals": [vital.to_dict() for vital in self.vitals]
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
            try_again = False
            response = co.generate(prompt=random_complaint, temperature=0.9, end_sequences=END_SEQUENCES)
            response_text = response[0].text
            start_quote_idx = response_text.find("\"")
            response_text = response_text[start_quote_idx + 1:]
            end_quote_idx = response_text.find("\"")
            response_text = response_text[:end_quote_idx]
            
            lower_case_response = response_text
            for phrase in BANNED_PHRASES:
                if phrase in lower_case_response:
                    try_again = True
            if try_again:
                continue
            else:
                break
        # print(random_complaint)
        return response_text
    
    def change_random_vitals(self):
        for vital in self.vitals:
            vital.change_random()
    
    def get_activities(self):
        message = "generate another, only give the json" if self.chat_history else ACTIVITIES_PROMPT
        response = co.chat(message=message, chat_history=self.chat_history, temperature=0.9)
        edited_text = response.text.replace("```", "").replace("json", "")
        try_again = True
        while try_again:
            try:
                json_dict = json.loads(edited_text)
                try_again = False
                activities = [activity for activity in json_dict["activities"]]
            except:
                response = co.chat(message=message, chat_history=self.chat_history)
                edited_text = response.text.replace("```", "").replace("json", "")
        self.chat_history.append({"role": "USER", "text": message})
        self.chat_history.append({"role": "CHATPOT", "text": edited_text})
        print(activities)
        return activities
