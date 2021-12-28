import json
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
    with open(filename) as f:
        data = json.load(f)
    return data


def save_file(filename, data):
    f = open(filename, "w")
    f.write(data)
    f.close()
    print("saving: "+filename)


# ----- uncomment these if you want to run this script on its own ----- #

#config = load_json("user-data.json")
#data = download_latest_crypto_data(config)
#save_file("crypto-data.json", json.dumps(data))
