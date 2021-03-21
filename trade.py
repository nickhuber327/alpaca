#Name:trade.py
#Author: Nick Huber
#Date: 20210312
#Trade with alpaca

import requests, json, config

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
POSITIONS_URL = "{}/v2/positions".format(BASE_URL)

def get_account():
    r = requests.get(ACCOUNT_URL, headers=config.HEADERS)
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
    "symbol" : symbol,
    "qty" : qty,
    "side" : side,
    "type": type,
    "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=config.HEADERS)
    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=config.HEADERS)
    return json.loads(r.content)

def get_positions():
    r = requests.get(POSITIONS_URL, headers=config.HEADERS)
    return json.load(r.content)

#orders = get_orders()
#response = create_order("AAPL", 100, "buy", "market", "gtc")

#account = get_account()

positions = get_positions()

print(positions)
