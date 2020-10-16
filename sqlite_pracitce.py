import sqlite3
import csv
from Employee import Employee

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE employees (first text, last text, payment integer)")


def add_emp(emp):
    with conn:
        cursor.execute("INSERT INTO employees VALUES (?, ?, ?)",
                       (emp.first_name, emp.last_name, emp.payment))


def find_emp_by_lastname(last_name):
    cursor.execute("SELECT * FROM employees WHERE last = :last",
                   {'last': last_name})
    return cursor.fetchall()


def update_payment(fullname, payment):
    with conn:
        cursor.execute(
            "UPDATE employees SET payment = :payment WHERE first = :first AND last = :last",
            {
                'first': fullname.split()[0],
                'last': fullname.split()[1],
                'payment': payment
            })


def remove_emp(fullname):
    with conn:
        cursor.execute(
            "DELETE FROM employees WHERE first = :first AND last = :last", {
                'first': fullname.split()[0],
                'last': fullname.split()[1]
            })


with open('employees.txt', 'r') as data_file:
    emp_generator = (Employee.from_string(single_line)
                     for single_line in data_file)
    for single_emp in emp_generator:
        cursor.execute(
            "INSERT INTO employees VALUES (?, ?, ?)",
            (single_emp.first_name, single_emp.last_name, single_emp.salary))

cursor.execute("SELECT * FROM employees WHERE payment < 4000")
result = cursor.fetchall()
print(result)

conn.close()