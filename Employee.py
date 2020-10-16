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
