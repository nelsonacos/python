#!/usr/bin/python3

import json
import requests

response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
data = json.loads(response.text)

top_10 = [i for i in data['data'].values() if i['rank'] <= 10]
with open('top10.json', 'w') as outfile:
    json.dump(top_10, outfile, indent=4, separators=(',', ': '))
