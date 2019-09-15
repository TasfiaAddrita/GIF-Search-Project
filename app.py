from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    # tenor_url = "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s"
    # submit = request.args.get('search')
    # TODO: Make 'params' dict with query term and API key
    params = {
        "apikey": 'STTZ6FZ9PGKF',
        "q": "cats",
        "lmt": 1,
        "media": "minimal"
    }

    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/search?", params=params)

    # TODO: Get the first 10 results from the search results
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        gif = json.loads(r.content)
        gif = gif['results'][0]
    else:
        gif = None

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template("index.html", gif=gif)

@app.route('/submit')
def get_gifs():
    submit = request.args.get('search')
    params = {
        "apikey": 'STTZ6FZ9PGKF',
        "q": submit,
        "lmt": 10,
        "media": "minimal"
    }
    r = requests.get("https://api.tenor.com/v1/search?", params=params)
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        gif = json.loads(r.content)
        gif = gif['results'][0]
    else:
        gif = None

    return render_template("index.html", gif=gif, name=submit)

if __name__ == '__main__':
    app.run(debug=True)
