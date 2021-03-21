#Name:history.py
#Author: Nick Huber
#Date: 20210320
#historical data

import config
import alpaca_trade_api as tradeapi

BASE_URL = "https://data.alpaca.markets/v2"

api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, BASE_URL, api_version='v2')

barset = api.get_barset('AAPL', 'day', limit=100)
aapl_bars = barset['AAPL']

aapl_open = aapl_bars[0].o
aapl_close = aapl_bars[-1].c

print(aapl_bars)
"""
BASE_URL = "https://data.alpaca.markets/v2"

def getHist(symbol, start, end, timeframe, limit=1000):
    HIST_URL = "{}/stocks/{}/bars".format(BASE_URL, symbol)
    data = {
        "start" : start,
        "end" : end,
        "limit": limit,
        "timeframe" : timeframe
    }
    r = requests.get(HIST_URL, json=data, headers=config.HEADERS)
    return json.loads(r.content)


hist = getHist("AAPL", "2000-03-25T17:39:39Z", "2021-03-00T16:00:00Z", "1Day")
print(hist)
"""
