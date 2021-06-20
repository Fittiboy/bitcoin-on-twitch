import json
import requests

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_token():
    """Captures the API token and saves it in settings.json"""
    # The API token is passed in the querystring as 'code'
    code = request.args.get('code')
    with open('settings.json') as settings_file:
        settings = json.load(settings_file)
        client_id = settings['client_id']
        client_secret = settings['client_secret']
        ip = settings['ip']
    redirect_uri = f"http://{ip}:6969"
    url = "https://streamlabs.com/api/v1.0/token"
    params = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
    }
    response = requests.post(url, data=params).json()
    print(response)
    token = response['access_token']
    with open('settings.json', 'w') as settings_file:
        settings['access_token'] = token
        json.dump(settings, settings_file, indent=4)

    return "Token added to settings.json! You should stop the server now!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)
