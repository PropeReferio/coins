import json
import os

import pandas as pd
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# CSV Must be organized in increasing order by ID

# Step 1: Get current crypto prices for each token in CSV
holdings = pd.read_csv("./crypto.csv", sep="|")


def get_current_prices():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    symbols = ",".join([str(num) for num in list(holdings.api_id)])
    parameters = {"id": f"{symbols}"}
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": os.environ["CMC_PRO_API_KEY"],
    }

    session = Session()
    session.headers.update(headers)

    current_prices = []

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        for coin in data["data"].values():
            # TODO Here, I should be able to get the current value
            # and multiply by the amount I have all in one iteration
            cur_price = coin["quote"]["USD"]["price"]
            current_prices.append(cur_price)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return current_prices


# Step 1a: Get current total value
def get_totals_in_usd(current_prices):
    totals_by_coin = []
    for i in range(len(holdings)):
        amount_held = json.loads(holdings.loc[i, "purchases"])[0]["amount"]
        value_of_coin = amount_held * current_prices[i]
        print(
            f"Coin: {holdings.loc[i, 'token']}, "
            f"Total value of coin: ${value_of_coin}"
        )
        totals_by_coin.append(value_of_coin)

    print(f"Totals of all holdings: {sum(totals_by_coin)}")


def main():
    current_prices = get_current_prices()
    get_totals_in_usd(current_prices)


main()

# Step 2: Calculate the total amount spent on crypto
# purchases (how to deal with sold crypto?
# Perhaps I should have a third column for sales, and subtract the
# total sales $ amount from total
# purchases $ amount? Otherwise, I could subtract highest value
# coin sales (in token amount) from
# the lowest value purchases (in token amount))

# Step 3: Display combined starting value of purchases with current value


# Later versions:
# 1) Choose which coins you want to compare
# 2) Make a graph, either hourly or daily
