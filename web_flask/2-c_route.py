#!/usr/bin/python3
"""this module creates starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def open_web():
    """open web and return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def open_web_2():
    """open web app on page hbnb and return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def get_c_text(text):
    """open web app on page c and print 'C <text>' """
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
