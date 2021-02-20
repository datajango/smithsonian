import requests
import os
import json
import save_json
from dotenv import load_dotenv

categories = [
    'culture',
    'data_source',
    'date',
    'object_type',
    'online_media_type',
    'place',
    'topic',
    'unit_code']

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_category_terms(category):
    """ Returns a JSOn response object for a given category """
    url = "https://api.si.edu/openaccess/api/v1.0/terms/{}?api_key={}".format(
        category, API_KEY)
    print(url)
    response = requests.get(url)
    print(response.status_code)
    return response.json()


def get_all_category_terms():
    """ Returns a dictionary for each category containing a list of terms """

    category_terms = {}

    for category in categories:
        data = get_category_terms(category)
        category_terms[category] = data

    save_json.save('all_category_terms', category_terms)


get_all_category_terms()
