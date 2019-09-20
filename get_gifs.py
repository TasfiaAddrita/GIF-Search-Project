from flask import request
import requests
from random import randint
import json

# calls tenor api, endpoints dependent on what user does
# input: tenor endpoint and user input
# output: dictionary of gifs and necessary request values
def get_gifs(endpoint, user_input):
    params = {
        "apikey": 'STTZ6FZ9PGKF',
        "limit": 10,
        "media_filter": "minimal"
    }

    # calls appropriate url based on user's input
    if endpoint == "search" or endpoint == "submit":
        params['q'] = user_input
        url = "https://api.tenor.com/v1/search?"
    elif endpoint == "trending":
        url = "https://api.tenor.com/v1/trending?"
    elif endpoint == "random":
        # choose a random category from the tenor api to generate random gifs
        r_categories = requests.get("https://api.tenor.com/v1/categories?", params=params)
        if r_categories.status_code == 200:
            categories = json.loads(r_categories.content)
            categories = categories['tags']
            random_category = categories[randint(0, len(categories))]["searchterm"]
            params['q'] = random_category
            url = "https://api.tenor.com/v1/random?"
        else:
            categories = None

    # requests gifs to tenor api
    r_gifs = requests.get(url, params=params)
    if r_gifs.status_code == 200:
        api_connection = True
        gif = json.loads(r_gifs.content)
        gif = gif['results']
        no_results = True if len(gif) == 0 else False
    else:
        api_connection = False

    jinja_template_values = {
        "gifs": gif,
        "no_results": no_results,
        "api_connection": api_connection,
        "search": user_input if user_input != None else None
    }

    return jinja_template_values
