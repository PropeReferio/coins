# Coins

This is a little CLI I made to get the total value of one's crypto holdings.

It works by using CoinMarketCap API: https://coinmarketcap.com/api/
It uses an encrypted CSV with rows in the following format:

`Stellar|512|[{"date":"", "amount": 14.1272323, "price/coin": 0}]`

You'll need to add the name of the Coin in the first column, the ID used by the API (found at this endpoint: https://pro-api.coinmarketcap.com/v1/cryptocurrency/map) in the second column, and to fill in "amount" in the json of the third column.

To encrypt your CSV, follow this tutorial: https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/

You'll need to have an environment variable that gives the path to the keyfile, and to have an encrypted named `enc.csv` at the project root.

### Env Vars
`CMC_PRO_API_KEY` needs to be set with your CoinMarketCap API Key.

`COINS_KEY_FILE_PATH` needs to be set with the path to the keyfile you generated with `cryptography.fernet.Fernet`.