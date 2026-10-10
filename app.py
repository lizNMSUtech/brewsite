from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/breweries")
def breweries():
    url = "https://api.openbrewerydb.org/v1/breweries?by_state=new_mexico&per_page=20"
    response = requests.get(url)
    brewery_list = response.json()
    return render_template("breweries.html", breweries=brewery_list)


if __name__ == "__main__":
    app.run(debug=True)