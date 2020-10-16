import requests
import json
import os

pay_load = {
    'access_key': '{}'.format(os.environ.get('CURRENCY_CONVERT_API_KEY'))
}

response = requests.get('http://data.fixer.io/api/latest',
                        params=pay_load).text

data_json = json.loads(response)
filter_currencies = dict()
for name, price in data_json['rates'].items():
    if price > 1 and price < 10:
        filter_currencies[name] = price
with open('EUR_price.json', 'w') as input_file:
    json.dump(filter_currencies, input_file, indent=2)
