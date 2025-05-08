import os
import tkinter as tk
from tkinterhtml import HtmlFrame
import googlemaps
from datetime import datetime
from flask import Flask, render_template


gmaps = googlemaps.Client(key=os.getenv("API_KEY_GOOGLE"))

app = Flask(__name__)

@app.route("/")
def map():
    with open("mp.html","r") as fp:
        content=fp.read()
        content=content.replace("YOUR_API_KEY",os.getenv("API_KEY_GOOGLE"))
    return content

if __name__ == "__main__":
    app.run(debug=True)