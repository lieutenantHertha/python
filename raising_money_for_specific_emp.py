import csv


class Employee(metaclass=type):
    raise_rate = 1.06

    def __init__(self, first_name, last_name, age, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position
        self.salary = salary

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email_address(self):
        return f'{self.first_name}_{self.last_name}@foxmail.com'

    @classmethod
    def constructor(cls, info):
        return cls(*tuple(info))


def Construction_From_File(filepath, method):
    with open(filepath, method) as data_file:
        csv_reader = csv.reader(data_file, delimiter=',')
        print('Field Names: {}'.format(next(csv_reader)))
        for single_line in csv_reader:
            if single_line:
                yield Employee.constructor(single_line)
            else:
                pass


'''This is the starting point of RAISING AMOUNT FOR ENGINEERS script'''

emp_generator = Construction_From_File('employees.csv', 'r')
filting_result = filter(
    lambda single_employee: single_employee.position == 'administrator',
    emp_generator)

modified_employees = map(
    lambda single_employee: Employee(
        single_employee.first_name, single_employee.last_name, single_employee.
        age, single_employee.position,
        round(float(single_employee.salary) * Employee.raise_rate, 2)),
    filting_result)

with open('raised_employees.csv', 'w', newline='') as input_file:
    csv_writer = csv.writer(input_file, delimiter=',')
    csv_writer.writerow(
        ['first_name', 'last_name', 'age', 'position', 'salary'])
    for each_employee in modified_employees:
        csv_writer.writerow([
            each_employee.first_name, each_employee.last_name,
            each_employee.age, each_employee.position, each_employee.salary
        ])
        print(each_employee.full_name, each_employee.age,
              each_employee.position, each_employee.salary)
