import json
import requests

from flask import Flask, request, abort
from pycoingecko import CoinGeckoAPI
from waitress import serve

app = Flask(__name__)

with open("settings.json") as settings_file:
    settings = json.load(settings_file)
    # This is the access token for the Streamlabs API
    access_token = settings["access_token"]
    # This is the currency that is converted to for Streamlabs
    fiat = settings["fiat"]


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
        data = request.get_json(force=True)
        # For logging and debugging, print incoming requests
        print(request, '\n', data)
        # The two LNbits extensions used return data in
        # different formats.  This try-except handles both.
        try:
            sats = int(data['amount'] / 1000)
            comment = data['comment']
        except KeyError:
            sats = int(data['amount'])
            comment = data['description']
        if not comment:
            comment = "No message!"
        amount = convert_to_fiat(sats, 'usd')
        url = "https://streamlabs.com/api/v1.0/donations"
        data = {
                "name": "bitcoin",
                "message": f"{str(sats)} sats: {comment}",
                "identifier": "bitcoin_donos",
                "amount": amount,
                "currency": fiat.upper(),
                "access_token": access_token,
        }
        response = requests.post(url, data=data)
        # For logging/debugging purposes
        print(response.json())
        return "Success!", 200
    else:
        abort(400)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5001)
