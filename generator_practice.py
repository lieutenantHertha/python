# This is a practicing script of generator expression.
import collections
import csv

City = collections.namedtuple('City', ['city_name', 'country', 'population', 'latitude', 'longtitude'])

with open('work_stack/worldcities.csv', 'r') as data_file:
    csv_reader = csv.DictReader(data_file)

    city_generator = (City(single_city['city_name'], single_city['country'], single_city['population'],
                           float(single_city['latitude']), float(single_city['longtitude'])) for single_city in csv_reader)

    city_counter = 0
    for city_info in city_generator:
        if city_info.country == 'United States' and int(city_info.population) > 1000000:
            city_counter += 1
            print(city_info.city_name, city_info.population)
    
    print('There are {} cities satisfied your criteria.'.format(city_counter))
