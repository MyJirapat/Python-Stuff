import requests

# Set the minimum and maximum prices at which to buy or sell each coin
min_prices = {"BTC": 8000, "ETH": 200, "BNB": 20}
max_prices = {"BTC": 9000, "ETH": 300, "BNB": 30}

# Get the current prices of each coin from an exchange API
prices = requests.get("https://api.exchange.com/v1/prices").json()

# Recommend buying each coin if the price is below the minimum
for coin, price in prices.items():
    if price < min_prices[coin]:
        print("Recommend buying {} at current price of {}".format(coin, price))

# Recommend selling each coin if the price is above the maximum
for coin, price in prices.items():
    if price > max_prices[coin]:
        print("Recommend selling {} at current price of {}".format(coin, price))
