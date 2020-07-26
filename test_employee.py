import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    #runs once before all tests
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    #runs once at the end
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    #sets up all the stuff here before every single test
    def setUp(self):
        print("setup")
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    #runs AFTER every test 
    #useful for file/database creation
    def tearDown(self):
        print("teardown")
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')

    def test_monthly_schedule(self):
        #use patch as a context manager
        with patch('employee.requests.get') as mocked_get:
            #will use mocked_get instead of return variable
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success!"

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, "Success!")
        
        with patch('employee.requests.get') as mocked_get:
            #will use mocked_get instead of return variable
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, "Bad Response!")


if __name__ == '__main__':
  unittest.main()