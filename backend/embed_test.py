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
