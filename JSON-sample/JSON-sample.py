#!/usr/bin/python3
import json
import requests

response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
data = json.loads(response.text)

finallist = []


def keep(data):
    for i in data['data'].values():
        if i['rank'] <= 10 and 1 <= i["quotes"]["USD"]["price"] <= 500:
            finallist.append(i)


keep(data)
#jsondata = json.dumps(finallist)
with open('top10.json', 'w') as outfile:
    json.dump(finallist, outfile, indent=4)
