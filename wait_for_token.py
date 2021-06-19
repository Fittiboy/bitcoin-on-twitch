import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_token():
    """Captures the API token and saves it in settings.json"""
    # The API token is passed in the querystring as 'code'
    token = request.args.get('code')
    with open('settings.json') as settings_file:
        settings = json.load(settings_file)
        settings['access_token'] = token
    with open('settings.json', 'w') as settings_file:
        json.dump(settings, settings_file, indent=4)

    return "Token added to settings.json! You should stop the server now!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)
