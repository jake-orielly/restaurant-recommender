from flask import Flask, request
from flask_cors import CORS
import requests as r
import json

app = Flask(__name__)
CORS(app)

yelp_url = 'https://api.yelp.com/v3'

with open("../credentials/bearer_token.txt") as file:
   bearer_token = file.read()

@app.route('/status')
def status():
    return 'Api is alive'

@app.route('/restaurants')
def restaurants():
    zipcode = request.args.get('zipcode')
    url = yelp_url + f"/businesses/search?location={zipcode}&open_now=true&limit=50"

    payload={}
    headers = {
    'Authorization': bearer_token
    }

    response = r.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)
