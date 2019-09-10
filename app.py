from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt)))

    # TODO: Make 'params' dict with query term and API key
params ={
apikey = 'STTZ6FZ9PGKF'


}
    # TODO: Make an API call to Tenor using the 'requests' library
    # set the apikey and limit
apikey = 'STTZ6FZ9PGKF'
lmt = 10



# continue a similar pattern until the user makes a selection or starts a new search.


    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html", message="Hello world!")


if __name__ == '__main__':
    app.run(debug=True)
