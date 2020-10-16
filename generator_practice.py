# This is a practicing script of generator expression.
import collections
import csv

City = collections.namedtuple('City', ['city_name', 'country', 'population', 'latitude', 'longtitude'])

with open('work_stack/worldcities.csv', 'r') as data_file:
    csv_reader = csv.DictReader(data_file)

    city_generator = (City(*single_city.values()) for single_city in csv_reader)

    city_counter = 0
    for city_info in city_generator:
        if city_info.population:
            if float(city_info.longtitude) < 0.0 and int(city_info.population) > 5000000:
                city_counter += 1
                print('{:20}{:15}{:10.4f}{:10.4f}'.format(city_info.city_name, 
                                                           city_info.population, 
                                                           float(city_info.latitude), 
                                                           float(city_info.longtitude)))
    
    print('There are {} cities satisfied your criteria.'.format(city_counter))
