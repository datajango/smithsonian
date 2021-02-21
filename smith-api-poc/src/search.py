import requests
import os
import json
import save_json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def search(text):
    url = "https://api.si.edu/openaccess/api/v1.0/search?q={}&api_key={}&rows=1000".format(
        text, API_KEY)
    print(url)
    response = requests.get(url)
    print(response.status_code)
    save_json.save(text, response.json())
    return response.json()
