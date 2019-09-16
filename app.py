from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""

    # TODO: Make 'params' dict with query term and API key
    params = {
        "apikey": 'STTZ6FZ9PGKF',
        "limit": 1,
        "media_filter": "minimal"
    }

    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/trending?", params=params)

    # TODO: Get the first 10 results from the search results
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        gif = json.loads(r.content)
        gif = gif['results']
    else:
        gif = None

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template("index.html", gifs=gif)

@app.route('/submit')
def get_gifs():
    submit = request.args.get('search')
    params = {
        "apikey": 'STTZ6FZ9PGKF',
        "q": submit,
        "limit": 10,
        "media_filter": "minimal"
    }
    r = requests.get("https://api.tenor.com/v1/search?", params=params)
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        gif = json.loads(r.content)
        gif = gif['results']
    else:
        gif = None

    return render_template("index.html", search=submit, gifs=gif)

if __name__ == '__main__':
    app.run(debug=True)
