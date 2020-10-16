import requests
import json
import csv
import os

article_params = {
    'q':
    'President Election',
    'from':
    '2020-10-16',
    'sortBy':
    'popularity',
    'apiKey':
    str(os.environ.get('NEWS_API_KEY')),
    'sources':
    'abc-news, bbc-news, bloomberg, cbs-news, cnn, fox-news, mashable, new-york-magazine'
}

res_string = requests.get('http://newsapi.org/v2/everything',
                          params=article_params).text.encode('utf-8')

articles_dict = json.loads(res_string)

with open('fetch_articles.csv', 'w', encoding='utf-8',
          newline='') as input_file:
    field_names = ['source', 'title', 'url', 'description']
    csv_writer = csv.DictWriter(input_file, fieldnames=field_names)
    csv_writer.writeheader()
    for single_article in articles_dict['articles']:
        single_article['source'] = single_article['source']['name']
        csv_writer.writerow({
            'source': single_article['source'],
            'title': single_article['title'],
            'url': single_article['url'],
            'description': single_article['description']
        })
        print(single_article['source'])
        print(single_article['title'])
        print(single_article['publishedAt'])
        print()