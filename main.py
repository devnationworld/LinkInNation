#!/usr/bin/env python3

from flask import Flask
from flask import render_template

# creates a Flask application
app = Flask(__name__)

@app.route("/")
def create_links():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)