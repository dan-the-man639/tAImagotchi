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




vitals = {
    "satiation": ["food", "eat", "hungry", "starving", "full", "fullness", "hunger", "eat", "ate", "eating", "meal", "snack", "snacks", "breakfast", "lunch", "dinner", "dessert"],
    "energy": ["tiring", "exercise", "physical", "train", "run", "walk", "sport", "baseball", "basketball", "soccer", "swim", "jump"],
    "happiness": ["happy", "joy", "fun", "friends", "social", "hobby", "relax", "play", "game", "card", "board", "video", "video game", "video games", "movie", "movies", "tv", "television", "show", "shows", "watch", "watching"],
    "intellect": ["smart", "intelligent", "knowledge", "learn", "learning", "learned", "study", "studying", "studied", "school", "college", "university", "universities", "class", "classes", "course", "courses", "subject", "subjects", "math", "science", "english", "history", "geography", "art", "music", "computer", "computers", "programming"]
}

satiation_embeddings = np.array(co.embed(vitals["satiation"], model="embed-english-v3.0", input_type="classification").embeddings)
energy_embeddings = np.array(co.embed(vitals["energy"], model="embed-english-v3.0", input_type="classification").embeddings)
happiness_embeddings = np.array(co.embed(vitals["happiness"], model="embed-english-v3.0", input_type="classification").embeddings)
intellect_embeddings = np.array(co.embed(vitals["intellect"], model="embed-english-v3.0", input_type="classification").embeddings)

embeddings = [satiation_embeddings, energy_embeddings, happiness_embeddings, intellect_embeddings]


def calculate_proj_len(activity):
    activity_embedding = np.array(co.embed([activity], model="embed-english-v3.0", input_type="classification").embeddings)
    proj_lens = []
    for arr in embeddings:
        sum = 0
        for i in range(len(arr)):
            cur_norm = np.linalg.norm(arr[i])
            sum += np.dot(activity_embedding, arr[i])/cur_norm
        avg = sum / len(arr) / len(activity_embedding)
        proj_lens.append(avg)
    return proj_lens
    


