import csv


def raise_amount(employee):
    return {
        'first_name': employee['first_name'],
        'last_name': employee['last_name'],
        'age': employee['age'],
        'position': employee['position'],
        'salary': round(1.05 * float(employee['salary']), 2)
    }


def engineer_filter(employee):
    return employee['position'] == 'engineer'


def artist_filter(employee):
    return employee['position'] == 'artist'


def administrator_filter(employee):
    return employee['position'] == 'administrator'


with open('employees.csv', 'r') as data_file:
    csv_reader = csv.DictReader(data_file)
    field_names = csv_reader.fieldnames

    employee_generator = (single_employee for single_employee in csv_reader)
    engineer_filter = filter(engineer_filter, employee_generator)
    raise_amount_map = map(raise_amount, engineer_filter)

    with open('engineers.csv', 'w', newline='') as input_file:
        csv_writer = csv.writer(input_file, delimiter=',')
        csv_writer.writerow(field_names)
        for each_engineer in raise_amount_map:
            csv_writer.writerow(each_engineer.values())