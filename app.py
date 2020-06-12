from flask import Flask, render_template, request
import requests
from random import randint
from get_gifs import get_gifs

app = Flask(__name__)

# when user enters home route or clicks random button, a grid of random gifs appears
@app.route('/')
def get_random_gifs():
    jinja_values = get_gifs("random", None)

    return render_template("index.html", gifs=jinja_values['gifs'], no_results=jinja_values['no_results'], api_connection=jinja_values['api_connection'])

# when user clicks trending button, a grid of trending gifs appears
@app.route('/trending')
def get_trending_gifs():
    jinja_values = get_gifs("trending", None)

    return render_template("index.html", gifs=jinja_values['gifs'], no_results=jinja_values['no_results'], api_connection=jinja_values['api_connection'])

# when user types in the search bar, a grid of gifs based on the user's input appears
@app.route('/search', methods=["POST"])
def search():
    search = request.form['search']
    jinja_values = get_gifs("search", search)

    return render_template("gifs.html", gifs=jinja_values['gifs'])

@app.route('/submit')
def get_derp_gifs():
    submit = request.args.get('search')
    jinja_values = get_gifs("submit", submit)

    return render_template(
        "index.html", 
        search=jinja_values['search'], 
        gifs=jinja_values['gifs'], 
        no_results=jinja_values['no_results'], 
        api_connection=jinja_values['api_connection']
    )

if __name__ == '__main__':
    app.run(debug=True)
