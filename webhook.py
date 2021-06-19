import json

from flask import Flask, request, abort
from pycoingecko import CoinGeckoAPI

app = Flask(__name__)

# This is the access token for the Streamlabs API
with open("access_token.json") as at_file:
    access_token = json.load(at_file)["access_token"]


def convert_to_fiat(sats: int, fiat: str) -> float:
    """Takes the amount of sats, and a fiat currency code
    and outputs the amount donated after fiat conversion"""
    cg = CoinGeckoAPI()
    price = cg.get_price(ids='bitcoin', vs_currencies=fiat)
    price = price['bitcoin'][fiat]
    # Price is in USD/BTC, while 1 sat = 10**-8 BTC
    amount = sats * price * (10**(-8))
    return amount


@app.route('/', methods=['POST'])
def webhook():
    """Handles incoming LNbits payments and pushes donations
    to the Streamlabs API"""
    if request.method == 'POST':
        pass
    else:
        abort(400)
