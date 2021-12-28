# cryptoticker

Simple python script that downloads crypto currency information from coinmarketcap.com

## Prerequisites

- API token generated from coinmarketcap.com (free version grants about 11 API calls/day)

## Install 

`pip3 install requirements.txt` - installs `requests` module

## run

1. Enter your data in `user-data_example.json` (& remove '_example' from the filename)

```
{
  "api_key": "your-coinmarketcap-api-key",
  "symbols": ["BTC","ETH","SOL","MATIC"],
  "currency": "EUR"
}
```

2. run `python3 downloader.py`, which downloads the crypto currency data and saves it as JSON in `crypto-data.json`
3. run `python3 cryptotracker.py` to display the selected currencies

