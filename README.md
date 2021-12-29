# cryptoticker

Simple python script that downloads crypto currency information from coinmarketcap.com and sends emails with summaries

* downloads current prices
* lets you specify which currencies you want to get info about
* lets you specify your personal portfolio and displays it's current worth
* sends you above data as a plain text email

## Prerequisites

- API token generated from coinmarketcap.com. Note that every time you run `downloader.py`, 'credits' are spend (depending on the amount of data returned), with a total limit of 333 credits per day (as of 2021-12-28)

## Install 

`pip3 install requirements.txt` - installs `requests` module

## Configure & Run

1. Enter your data in `user-data_example.json` (& remove `_example` from the filename)

```
{
  "api_key": "your-coinmarketcap-api-key",
  "symbols": ["BTC","ETH","SOL","MATIC"],
  "currency": "EUR",
  "portfolio": [
    {
      "symbol": "BTC",
      "amount": 0.50,
      "cost": 10
    },
    {
      "symbol": "ETH",
      "amount": 1.0,
      "cost": 10
    }
  ]
}
```

* `api_key`: the token you generate on coinmarketcap.com
* `symbols`: the crypto currencies you like to include in your email report
* `currency`: which fiat currency (e.g. EUR, USD) to convert to
* `portfolio`: your personal assets (which crypto, amount of that crypto you own, how much you paid for it)

2. configure `email.json` 

```
{
  "email_from": "",
  "email_from_password": "",
  "email_from_smtp": "",
  "email_from_port": 587,
  "email_to_default": ""
}
```

* `email_from`: the email address used for sending the email
* `email_from_password`: the password for the email address
* `email_from_smtp`: the smtp server of your email provider
* `email_from_port`: the smtp port of your email provider (defaults to 587)
* `email_to`: where to send the email to

3. run `python3 downloader.py`, which downloads the crypto currency data and saves it as JSON in `crypto-data.json`
4. run `python3 tracker.py` to display the selected currencies and send an email

Note that `crypto-data.json` will contain at least 100 data points, which might be much more than the crypto currencies specified in your `user-data.json`. The symbols list there is only needed for displaying your favorites when running `tracker.py`.

To make this script more convenient for cron job execution, `crypto.py` has been added, which executes both scripts. Therefore, some commands in `downloader.py` and `tracker.py` have been commented out. If you still want to execute these scripts independent from each other (which would make sense if you e.g. want other options than to send emails), just uncomment the last lines in each files.

## Setup a cron job (e.g. on Raspberry PI)

good tutorial here: https://medium.com/@gavinwiener/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e

`crontab -e`

Add a line, e.g. mine is every day at 07:00

`00 07 * * * /usr/bin/python3 /home/pi/code/cryptoticker/crypto.py`

## Output

If everything is configured correct, you should get an email that looks like this (and of course you can config it to your personal liking):

```
Here is your executive summary for today:

Crypto prices:
Bitcoin (BTC)	    42510.55 EUR 	▼ -3.2%
Ethereum (ETH)	    3384.51 EUR 	▼ -2.65%
Solana (SOL)	    157.37 EUR 	        ▼ -6.92%
Polygon (MATIC)	    2.27 EUR 	        ▼ -3.33%

Portfolio:
Currency 	    Worth         Profit/Loss	  Return
Bitcoin (BTC)	    2155.0 EUR	  231.92 EUR	  12.06%
Ethereum (ETH)	    102.85 EUR	  -285.18 EUR	  -73.49%
Solana (SOL)	    1185.28 EUR	  399.26 EUR	  50.8%
Polygon (MATIC)	    669.12 EUR	  268.11 EUR	  66.86%

Total		    4112.25 EUR	  614.11 EUR
```

   

