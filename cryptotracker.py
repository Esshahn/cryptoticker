

import json
import smtplib


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


def format_crypto_data(symbols, crypto):
    msg = ""
    for symbol in symbols:
        item = find_symbol_in_list(symbol, crypto)
        if item is not None:
            if item["quote"]["EUR"]["percent_change_24h"] < 0:
                trend = "down"
            else:
                trend = "up"
            msg += str(item["name"] + " (" + item["symbol"]) + "): "
            msg += str(round(item["quote"]["EUR"]
                             ["price"], 2)) + " EUR, " + trend + " "
            msg += str(round(item["quote"]["EUR"]
                             ["percent_change_24h"], 2))+"%"
            msg += "\n"
        else:
            print("Symbol not found: "+symbol)
    print(msg)
    return msg


def send_mail(bodymsg, email):
    subject = f'Your crypto update'
    body = "Here is your executive summary for today:\n\n"
    body += bodymsg
    msg = f'Subject: {subject}\n\n{body}'

    server = smtplib.SMTP(email["email_from_smtp"], email["email_from_port"])
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email["email_from"], email["email_from_password"])
    server.sendmail(email["email_from"], email["email_to"], msg.encode('utf8'))
    server.quit()


# ------------------ main ------------------ #


crypto_all = load_json("crypto-data.json")
crypto = crypto_all["data"]
user_all = load_json("user-data.json")
symbols = user_all["symbols"]
email = load_json('email.json')

body = format_crypto_data(symbols, crypto)
send_mail(body, email)
