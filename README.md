# cryptoticker

Simple python script that downloads crypto currency information from coinmarketcap.com and sends emails with summaries

* downloads current prices
* lets you specify which currencies you want to get info about
* lets you specify your personal portfolio and displays it's current worth
* sends you above data as a plain text email

## Prerequisites

- API token generated from coinmarketcap.com (free version grants about 13 API calls/day). Note that every time you run `downloader.py`, 'credits' are spend (depending on the amount of data returned), with a total limit of 333 credits per day (as of 2021-12-28)

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
      "amount": 0.50
    },
    {
      "symbol": "ETH",
      "amount": 1.0
    }
  ]
}
```

* `api_key`: the token you generate on coinmarketcap.com
* `symbols`: the crypto currencies you like to include in your email report
* `currency`: which fiat currency (e.g. EUR, USD) to convert to
* `portfolio`: your personal assets

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



   

