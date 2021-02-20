import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def save(text, str_data):
    filename = "{}.json".format(text)
    with open(filename, 'w') as outfile:
        data  = json.dumps(str_data, indent=4)
        outfile.write(data)

def search(text):
    url = "https://api.si.edu/openaccess/api/v1.0/search?q={}&api_key={}".format(text, API_KEY)
    print(url)
    response = requests.get(url)
    print(response.status_code)
    save(text, response.json())

search('entomology')