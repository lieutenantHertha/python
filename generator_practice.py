# This is a practicing script of generator expression.
import collections
import csv

City = collections.namedtuple('City', ['city_name', 'country', 'population', 'latitude', 'longtitude'])

with open('work_stack/worldcities.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)

    city_generator = (City(*single_line) for single_line in csv_reader)
    for single_city in city_generator:
        if single_city.city_name == 'Zhengzhou':
            print(single_city)




