import json
import os

from requests import Session

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

parameters = {"symbol": "MATIC,XLM,COMP,BAL,CLV,GRT,ANKR,BOND,SKL,NU,FORTH"}
# TODO Add argparse with --find, -f to get IDs for symbols passed in

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": os.environ["CMC_PRO_API_KEY"],
}

session = Session()
session.headers.update(headers)

current_prices = []

response = session.get(url, params=parameters)
data = json.loads(response.text)["data"]

for coin in data:
    print(f"Coin: {coin['name']}, Symbol: {coin['symbol']}, ID: {coin['id']}")
