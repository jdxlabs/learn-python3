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
            "Chewbacca",
            "Darth",
            "Obi-Wan",
        ]
    })


if __name__ == '__main__':
    app.run(port=3000, debug=True)

# Command to launch Flash on port 3000 :
# flask run --port=3000 --host=0.0.0.0 --with-threads --reload --debugger --no-reload
