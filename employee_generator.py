import random
import csv

field_names = ['first_name', 'last_name', 'age', 'position', 'salary']
positions = [
    'engineer', 'artist', 'administrator', 'manager', 'advertiser',
    'financial', 'sales', 'security', 'law', 'maintainer'
]
position_weights = [40, 20, 10, 5, 5, 4, 8, 4, 2, 2]

with open('name.txt', 'r') as name_data:
    with open('employees.csv', 'w', newline='') as input_file:
        csv_writer = csv.DictWriter(input_file,
                                    fieldnames=field_names,
                                    delimiter=',')
        csv_writer.writeheader()
        for single_line in name_data:
            first_name, last_name = single_line.split(' ')
            age = random.randint(20, 51)
            position = random.choices(positions, k=1, weights=position_weights)
            salary = random.randint(2000, 4000) + age * 100
            csv_writer.writerow({
                'first_name': first_name.strip(),
                'last_name': last_name.strip(),
                'age': age,
                'position': position[0],
                'salary': salary
            })
