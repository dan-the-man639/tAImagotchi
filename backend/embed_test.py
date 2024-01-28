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




with open("activities.json", "r") as file:
    data = json.load(file)
    activities = data["activities"]

vitals = {
    "satiation": ["food", "eat", "hungry", "starving", "full", "fullness", "hunger", "eat", "ate", "eating", "meal", "snack", "snacks", "breakfast", "lunch", "dinner", "dessert"],
    "energy": ["tiring", "exercise", "physical", "train", "run", "walk", "sport", "baseball", "basketball", "soccer", "swim", "jump"],
    "happiness": ["happy", "joy", "fun", "friends", "social", "hobby", "relax", "play", "game", "card", "board", "video", "video game", "video games", "movie", "movies", "tv", "television", "show", "shows", "watch", "watching"],
    "intellect": ["smart", "intelligent", "knowledge", "learn", "learning", "learned", "study", "studying", "studied", "school", "college", "university", "universities", "class", "classes", "course", "courses", "subject", "subjects", "math", "science", "english", "history", "geography", "art", "music", "computer", "computers", "programming"]
}

print(activities)
activities_embeddings = np.array(co.embed(activities, model="embed-english-light-v2.0").embeddings)
satiation_embeddings = np.array(co.embed(vitals["satiation"], model="embed-english-light-v2.0").embeddings)
energy_embeddings = np.array(co.embed(vitals["energy"], model="embed-english-light-v2.0").embeddings)
happiness_embeddings = np.array(co.embed(vitals["happiness"], model="embed-english-light-v2.0").embeddings)
intellect_embeddings = np.array(co.embed(vitals["intellect"], model="embed-english-light-v2.0").embeddings)

embeddings = [satiation_embeddings, energy_embeddings, happiness_embeddings, intellect_embeddings]


for idx, arr in enumerate(embeddings):
    sum = 0
    for i in range(len(arr)):
        print("hello")
        cur_norm = np.linalg.norm(arr[i])
        for j in range(len(activities_embeddings)):
            sum += np.dot(activities_embeddings[j], arr[i])/cur_norm
    avg = sum / len(arr) / len(activities_embeddings)
    print(list(vitals.keys())[idx], avg)


