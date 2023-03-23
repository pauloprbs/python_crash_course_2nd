import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Paulo Renato", "Baliza Silva", 12_000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 17_000)

    def test_give_custom_raise(self):
        self.employee.give_raise(4_000)
        self.assertEqual(self.employee.annual_salary, 16_000)

if __name__ == "__main__":
    unittest.main()