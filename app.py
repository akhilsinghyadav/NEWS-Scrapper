from flask import Flask, jsonify
from flask_cors import CORS
from thehindu import _get_the_hindu
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from indianexpress import _get_the_express

app = Flask(__name__)
CORS(app)

NEWS_SOURCES = {
    "TheHindu": "https://www.thehindu.com/latest-news/",
    "IndianExpress": "https://edition.cnn.com/",
    # "Reuters": "https://www.reuters.com/"
}



@app.route("/headlines_ie", methods=["GET"])
def get_headlines_ie():
    news_data = _get_the_express()
    return jsonify(news_data)
@app.route("/headlines_th", methods=["GET"])
def get_headlines_th():
    news_data = _get_the_hindu()
    return jsonify(news_data)

if __name__ == "__main__":   
    app.run(debug=True)
