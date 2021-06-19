import json

from subprocess import run
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
        d = "name=bitcoin" \
            f"&message={str(sats)} sats: {comment}" \
            f"&identifier=bitcoin_donos" \
            f"&amount={amount}" \
            f"&currency={fiat.upper()}" \
            f"&access_token={access_token}"
        # For some reason, I had issues making a valid request
        # with Python's requests library. Please feel free to
        # fix this. For now, curl works!
        curl = f"curl --request POST --url {url} -d \"{d}\""
        response = run(curl, shell=True, capture_output=True)
        # For logging/debugging purposes
        print(curl)
        print(response.stdout)
        return "Success!", 200
    else:
        abort(400)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5001)
