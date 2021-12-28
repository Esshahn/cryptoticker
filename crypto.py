from tracker import *
from downloader import *


# ------------------ downloader ------------------ #


config = load_json("user-data.json")
data = download_latest_crypto_data(config)
save_file("crypto-data.json", json.dumps(data))


# ------------------ tracker ------------------ #


crypto_all = load_json("crypto-data.json")
crypto = crypto_all["data"]
user_all = load_json("user-data.json")
symbols = user_all["symbols"]
portfolio = user_all["portfolio"]
email = load_json('email.json')

full_portfolio = create_portfolio(portfolio, crypto)
body = format_crypto_data(symbols, crypto)
body += format_portfolio(full_portfolio)

send_mail(body, email)
