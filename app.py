from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

@app.route("/")
def index():
    number = random.randint(1,1000)
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    data = response.json()
    trivia = data["text"]
    return render_template("index.html",trivia=trivia)

if __name__ == "__main__":
    app.run(debug=True)