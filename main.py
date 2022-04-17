from requests import get
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)





@app.route("/", methods=["GET"])
def home():

    return render_template("index.html", ip = get('https://api.ipify.org').text)

if __name__ == "__main__":
    app.run()