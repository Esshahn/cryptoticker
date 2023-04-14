import json
import sys
import requests


def download_latest_crypto_data(config):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        "convert": config["currency"],
    }
    headers = {
        "X-CMC_PRO_API_KEY": config["api_key"],
        "Accept": "application/json"
    }
    response = requests.get(url, params=parameters, headers=headers)
    data = response.json()
    return data


def load_json(filename):
    # load JSON
    with open(sys.path[0] + '/' + filename) as json_file:
        json_data = json.load(json_file)
    return json_data


def save_file(filename, data):
    f = open(sys.path[0] + '/' + filename, "w")
    f.write(data)
    f.close()
    print("saving: "+filename)