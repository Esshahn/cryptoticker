# cryptoticker

Simple python script that downloads crypto currency information from coinmarketcap.com

## Prerequisites

- API token generated from coinmarketcap.com (free version grants about 13 API calls/day). Note that every time you run `downloader.py`, 'credits' are spend (depending on the amount of data returned), with a total limit of 333 credits per day (as of 2021-12-28)

## Install 

`pip3 install requirements.txt` - installs `requests` module

## run

1. Enter your data in `user-data_example.json` (& remove `_example` from the filename)

```
{
  "api_key": "your-coinmarketcap-api-key",
  "symbols": ["BTC","ETH","SOL","MATIC"],
  "currency": "EUR"
}
```

2. run `python3 downloader.py`, which downloads the crypto currency data and saves it as JSON in `crypto-data.json`
3. run `python3 cryptotracker.py` to display the selected currencies


Note that `crypto-data.json` will contain at least 100 data points, which might be much more than the crypto currencies specified in your `user-data.json`. The symbols list there is only needed for displaying your favorites when running `cryptotracker.py`.

