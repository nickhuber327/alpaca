import config, requests, json, csv
from datetime import datetime

TICKER = "AAPL"
START_DATE = '2019-01-01'
END_DATE = '2021-03-19'
POLYGON_URL = 'https://api.polygon.io/v2/aggs/ticker/{}/range/1/day/{}/{}?apiKey={}'

r = requests.get(POLYGON_URL.format(TICKER, START_DATE, END_DATE, config.API_KEY))

data = json.loads(r.content)

print("date, open, high, low, close")

for item in data['results']:
    formatted_date = datetime.fromtimestamp(item['t'] / 1000)
    date_only = formatted_date.strftime('%Y-%m-%d')

    print("{},{},{},{},{}".format(date_only, item['o'], item['h'], item['l'], item['c']))
