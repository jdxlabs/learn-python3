#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/characters", methods=["GET"])
def caracters():
    return jsonify({
        "Characters": [
            "Luke",
            "Leia",
            "Han",
            "Chewbacca"
        ]
    })


if __name__ == '__main__':
    app.run(port=1235, debug=True)
