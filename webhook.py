import json

from flask import Flask, request, abort
from pycoingecko import CoinGeckoAPI

app = Flask(__name__)

with open("access_token.json") as at_file:
    access_token = json.load(at_file)["access_token"]


def convert_to_fiat(sats, fiat):
    cg = CoinGeckoAPI()
    price = cg.get_price(ids='bitcoin', vs_currencies=fiat)
    price = price['bitcoin'][fiat]
    amount = sats * price * (10**(-8))
    return amount


@app.route('/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        pass
    else:
        abort(400)
