from flask import Flask, render_template, request
import requests
import json
from random import randint

app = Flask(__name__)

@app.route('/')
def get_random_gifs():

    params = {
        "apikey": 'STTZ6FZ9PGKF',
        "limit": 10
    }
    r_categories = requests.get("https://api.tenor.com/v1/categories?", params=params)
    if r_categories.status_code == 200:
        categories = json.loads(r_categories.content)
        categories = categories['tags']
        # print(categories)
        random_category = categories[randint(0, len(categories))]["searchterm"]
        # print(random_category)
        params['q'] = random_category
    else:
        categories = None

    r_gifs = requests.get("https://api.tenor.com/v1/random?", params=params)
    if r_gifs.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        api_connection = True
        gif = json.loads(r_gifs.content)
        gif = gif['results']
        no_results = True if len(gif) == 0 else False
    else:
        api_connection = False
    return render_template("index.html", gifs=gif, no_results=no_results, api_connection=api_connection)


# @app.route('/input', methods=['POST'])
# def get_input():
#     input = request.form['q']
#     return input

@app.route('/submit')
def get_gifs():
    submit = request.args.get('search')
    # submit = request.args.get('')
    params = {
        "apikey": 'STTZ6FZ9PGKF',
        "q": submit,
        "limit": 10,
        "media_filter": "minimal"
    }
    r = requests.get("https://api.tenor.com/v1/search?", params=params)
    # print(r)
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        api_connection = True
        gif = json.loads(r.content)
        gif = gif['results']
        no_results = True if len(gif) == 0 else False
    else:
        api_connection = False
    return render_template("index.html", search=submit, gifs=gif, no_results=no_results, api_connection=api_connection)

@app.route('/trending')
def get_trending_gifs():
    params = {
        "apikey": 'STTZ6FZ9PGKF',
        "media_filter": "minimal"
    }
    r = requests.get("https://api.tenor.com/v1/trending?", params=params)
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        api_connection = True
        gif = json.loads(r.content)
        gif = gif['results']
        no_results = True if len(gif) == 0 else False
    else:
        api_connection = False
    return render_template("index.html", gifs=gif, no_results=no_results, api_connection=api_connection)

@app.route('/search', methods=["POST"])
def search():
    search = request.form['search']
    params = {
        "apikey": 'STTZ6FZ9PGKF',
        "q": search,
        "limit": 10,
        "media_filter": "minimal"
    }
    r = requests.get("https://api.tenor.com/v1/search?", params=params)

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        api_connection = True
        gif = json.loads(r.content)
        gif = gif['results']
        no_results = True if len(gif) == 0 else False
    else:
        api_connection = False

    return render_template("gifs.html", gifs=gif)

if __name__ == '__main__':
    app.run(debug=True)
