#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "API is running..."

@app.route("/users", methods=["GET"])
def caracters():
    return jsonify({
        "users": [
            "Luke",
            "Leia",
            "Han",
            "Chewi",
            "Darth",
            "Obi",
        ]
    })


if __name__ == '__main__':
    app.run(port=3000, debug=True)
