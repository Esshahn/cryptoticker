# curl -H "X-CMC_PRO_API_KEY: dd99003f-3bcf-4a24-9c23-c809389b4c1d" -H "Accept: application/json" -d "start=1&limit=5000&convert=EUR" -G https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest

import json


def load_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data["data"]


def save_file(filename, data):
    f = open(filename, "w")
    f.write(data)
    f.close()
    print("saving: "+filename)


def find_symbol_in_list(symbol, list):
    for item in list:
        if item["symbol"] == symbol:
            return item
    return None


def display_crypto_data(symbols, crypto):
    for symbol in symbols:
        item = find_symbol_in_list(symbol, crypto)
        if item is not None:
            print(item["symbol"])
            print(item["name"])
            print("EUR: "+str(round(item["quote"]["EUR"]["price"], 2)))
            print(
                str(round(item["quote"]["EUR"]["percent_change_24h"], 2))+"%")
            print("")
        else:
            print("Symbol not found: "+symbol)


crypto = load_json("list.json")

symbols = ["BTC", "ETH", "SOL", "MATIC"]
display_crypto_data(symbols, crypto)
