

import json
import sys
import smtplib
from datetime import datetime,timedelta


def load_json(filename):
    # load JSON
    with open(sys.path[0] + '/' + filename) as json_file:
        json_data = json.load(json_file)
    return json_data


def find_symbol_in_list(symbol, list):
    for item in list:
        if item["symbol"] == symbol:
            return item
    return None


def format_crypto_data(symbols, crypto):
    msg = "Crypto prices:\n"
    for symbol in symbols:
        item = find_symbol_in_list(symbol, crypto)
        if item is not None:
            msg += str(item["name"] + " (" + item["symbol"]) + ")\t"
            msg += str(round(item["quote"]["EUR"]
                             ["price"], 2)) + " EUR \t"
            msg += str(round(item["quote"]["EUR"]
                             ["percent_change_24h"], 2))+"%"
            msg += "\n"
        else:
            print("Symbol not found: "+symbol)
    msg += "\n"
    print(msg)
    return msg


def create_portfolio(portfolio, crypto):
    for item in portfolio:
        item["price"] = find_symbol_in_list(item["symbol"], crypto)[
            "quote"]["EUR"]["price"]
        item["value"] = round(item["price"] * item["amount"], 2)
        item["name"] = find_symbol_in_list(item["symbol"], crypto)[
            "name"]
    return portfolio


def format_portfolio(portfolio,history):
    msg = "Portfolio:\n"
    msg += "Currency \tWorth\t\tProfit/Loss\tReturn\n"
    total_worth = 0
    total_profit = 0

    for item in portfolio:
        msg += str(item["name"] + " (" + item["symbol"]) + ")\t"
        msg += str(round(item["value"], 2)) + " EUR"
        msg += "\t" + str(round(item["value"]-item["cost"], 2)) + " EUR"
        msg += "\t" + \
            str(round(((item["value"]-item["cost"]) /
                       item["cost"]*100), 2)) + "%"
        msg += "\n"
        total_worth += item["value"]
        total_profit += item["value"]-item["cost"]
    msg += "\nTotal\t\t" + str(round(total_worth, 2)) + " EUR"
    msg += "\t" + str(round(total_profit, 2)) + " EUR"

    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
    history.update({today: {"total_worth": total_worth}})
    f = open(sys.path[0] + '/history.json', "w")
    f.write(json.dumps(history))
    f.close()
    
    
    try:
        total_worth_yesterday = history[yesterday]["total_worth"]
        daily_profit = round(total_worth - total_worth_yesterday, 2)
        msg += "\nDaily profit:\t" + str(daily_profit) + " EUR"
    except:
        pass

    print(msg)
    return msg


def tab(item):
    return "\t" + item


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


# ----- uncomment these if you want to run this script on its own ----- #

#crypto_all = load_json("crypto-data.json")
#crypto = crypto_all["data"]
#user_all = load_json("user-data.json")
#symbols = user_all["symbols"]
#portfolio = user_all["portfolio"]
#email = load_json('email.json')

#full_portfolio = create_portfolio(portfolio, crypto)
#body = format_crypto_data(symbols, crypto)
#body += format_portfolio(full_portfolio)

#send_mail(body, email)
