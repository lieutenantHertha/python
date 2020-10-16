<<<<<<< HEAD
class Employee:
    raise_amount_rate = 1.05
    social_security_rate = 0.08

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.social_security = 0.0

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first_name,
                                                 self.last_name, self.salary)

    def __str__(self):
        return "{}--{}--{}".format(self.full_name, self.email_address,
                                   self.salary)

    @property
    def full_name(self):
        return "{}.{}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        self.first_name, self.last_name = name.split(".")
        print("The employee has been renamed.")

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None
        print("The employee's full name has been deleted.")

    @property
    def email_address(self):
        return "{}.{}@gmail.com".format(self.first_name, self.last_name)

    def raise_amount(self):
        self.salary *= Employee.raise_amount_rate
        return self.salary

    def pay_security(self):
        self.social_security += self.salary * Employee.social_security_rate
        return self.social_security

    # This is class method which accepts cls as The Abstract Class by default, programmers usually use it as alternative constructor.
    @classmethod
    def from_string(cls, info_msg):
        first_name, last_name, salary = info_msg.split("-")
        return cls(first_name, last_name, salary)

    @classmethod
    def change_raise_amt(cls, raise_amt):
        cls.raise_amount_rate = raise_amt


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, level):
        super().__init__(first_name, last_name, salary)
        self.level = level


class Programmer(Employee):
    def __init__(self, first_name, last_name, salary, language):
        super().__init__(first_name, last_name, salary)
        self.language = language
=======
import datetime
import pytz


class Employee:
    raise_amount = 1.05

    def __init__(self, first, last, payment):
        self.first_name = first
        self.last_name = last
        self.payment = payment

    @property
    def full_name(self):
        return '{}.{}'.format(self.first_name, self.last_name)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first_name, self.last_name)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.payment)

    def __str__(self):
        return '{}-{}-{}'.format(self.first_name, self.last_name, self.payment)

    @classmethod
    def constructor(cls, message_string):
        first, last, payment = message_string.split('-')
        return cls(first, last, payment)

    @staticmethod
    def datetime():
        print('Time: {}'.format(datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai'))))

    def raise_payment(self):
        self.payment = self.payment * Employee.raise_amount


class Developer(Employee):
    def __init__(self, first, last, payment, language):
        super().__init__(first, last, payment)
        self.language = language

    def __repr__(self):
        return "Developer('{}', '{}', {}, '{}')".format(self.first_name, self.last_name, self.payment, self.language)


class Manager(Employee):
    def __init__(self, first, last, payment, subordinate=None):
        super().__init__(first, last, payment)
        if not subordinate:
            self.subordinate = []
        else:
            self.subordinate = subordinate

    def __repr__(self):
        return "Manager('{}', '{}', {}, {})".format(self.first_name, self.last_name, self.payment, self.subordinate)

    def add(self, employee):
        if employee not in self.subordinate:
            self.subordinate.append(employee)
        else:
            print('The employee is already in the subordinate list.')

    def remove(self, name):
        for single_emp in self.subordinate:
            if single_emp.full_name == name:
                self.subordinate.remove(single_emp)


dev_1 = Developer('Anita', 'Mui', 89000, 'python')
dev_2 = Developer('Taylor', 'Swift', 85000, 'Ruby')
dev_3 = Developer('Josephine', 'Howell', 90000, 'C++')
mngr = Manager('Avril', 'Sweden', 100000)

for single_dev in [dev_1, dev_2, dev_3]:
    mngr.add(single_dev)

for each_emp in mngr.subordinate:
    each_emp.raise_payment()
    print(each_emp.full_name, each_emp.payment)


>>>>>>> c90fcfbda7cdf314ac7fb55f5ac27d97869ac075
