import requests
import json
import csv
import os

params = {
    'apiKey': str(os.environ['NEWS_API_KEY']),
    'language': 'en',
    'country': 'us'
}

response = requests.get('https://newsapi.org/v2/sources', params=params)
info_sources = json.loads(response.text)

if info_sources['status'] == 'ok':
    field_names = list(info_sources['sources'][0].keys())

    with open('info_sources.csv', 'w', newline='') as input_file:
        csv_writer = csv.DictWriter(input_file,
                                    fieldnames=field_names,
                                    delimiter=',')
        csv_writer.writeheader()
        for single_source in info_sources['sources']:
            csv_writer.writerow(single_source)
elif response.status_code >= 400:
    raise ConnectionError('Not accessible resource')
elif info_sources['status'] == 'error':
    raise Exception('Some url parameters might be wrong.')