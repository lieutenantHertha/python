import unittest
import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee.Employee('Anita', 'Mui', 95000)
        self.emp_2 = Employee.Employee('Jacqueline', 'Iverson', 75000)
        print('Set Up For Single Test')

    def tearDown(self):
        print('Tear Down For Single Test')

    def test_full_name(self):
        self.assertEqual(self.emp_1.full_name, 'Anita.Mui')
        self.assertEqual(self.emp_2.full_name, 'Jacqueline.Iverson')

        self.emp_1.first_name = 'Avira'
        self.emp_2.first_name = 'Jefferson'

        self.assertEqual(self.emp_1.full_name, 'Avira.Mui')
        self.assertEqual(self.emp_2.full_name, 'Jefferson.Iverson')

    def test_email_address(self):
        self.assertEqual(self.emp_1.email_address, 'Anita.Mui@gmail.com')
        self.assertEqual(self.emp_2.email_address,
                         'Jacqueline.Iverson@gmail.com')

        self.emp_1.first_name = 'Avira'
        self.emp_2.first_name = 'Jefferson'

        self.assertEqual(self.emp_1.email_address, 'Avira.Mui@gmail.com')
        self.assertEqual(self.emp_2.email_address,
                         'Jefferson.Iverson@gmail.com')

    def test_raise_amount(self):
        self.assertEqual(self.emp_1.salary, 95000)
        self.assertEqual(self.emp_2.salary, 75000)

        self.emp_1.raise_amount()
        self.emp_2.raise_amount()

        self.assertEqual(self.emp_1.salary,
                         95000 * Employee.Employee.raise_amount_rate)
        self.assertEqual(self.emp_2.salary,
                         75000 * Employee.Employee.raise_amount_rate)


if __name__ == '__main__':
    unittest.main()