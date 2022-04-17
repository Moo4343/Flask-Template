from requests import get
from crypt import methods
from flask import Flask, render_template, request, jsonify
from crypt import *
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    ip = get('https://api.ipify.org').text
    return render_template("index.html", ip = get('https://api.ipify.org').text)

if __name__ == "__main__":
    app.run()