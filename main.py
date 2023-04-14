# -------------------------------------------------
# Cryptoticker
# Python Script to get the current prices of crypto currencies
# and send an email with the current prices
# 2023 Ingo Hinterding
# https://github.com/Esshahn/cryptoticker
# -------------------------------------------------

from tracker import *
from downloader import *
import os

# ------------------ downloader ------------------ #


config = load_json("user-data.json")
data = download_latest_crypto_data(config)
save_file("crypto-data.json", json.dumps(data["data"]))


# ------------------ tracker ------------------ #

def create_history():
  # create history file if not exists
  filename = "history.json"
  if not os.path.isfile(filename):
    dummy_data = json.dumps({"0000-00-00":{"total_worth":0}})
    with open(filename, "w") as file:
        file.write(dummy_data)
    print("Neue Datei erstellt:", filename)
  

def main():
  create_history()
  crypto = load_json("crypto-data.json")
  history = load_json("history.json")
  user_all = load_json("user-data.json")
  symbols = user_all["symbols"]
  portfolio = user_all["portfolio"]
  email = load_json('email.json')

  full_portfolio = create_portfolio(portfolio, crypto)
  body = format_crypto_data(symbols, crypto)
  body += format_portfolio(full_portfolio,history)

  send_mail(body, email)

if __name__ == "__main__":
  main()
