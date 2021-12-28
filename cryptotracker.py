

import json


def load_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


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


crypto_all = load_json("crypto-data.json")
crypto = crypto_all["data"]

user_all = load_json("user-data.json")
symbols = user_all["symbols"]
display_crypto_data(symbols, crypto)
