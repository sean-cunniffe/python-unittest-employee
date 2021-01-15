# Created By SEAN CUNNIFFE on 14/01/2021

from unittest import TestCase
from unittest.mock import patch
from employee import Employee


class TestEmployee(TestCase):

    # runs before each test
    def setUp(self) -> None:
        self.employee_1 = Employee('Sean', 'Cunniffe', 30000)
        self.employee_2 = Employee('John', 'Doe', 35000)

    # runs after each test
    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_fullname(self):
        self.assertEqual(self.employee_1.first, 'Sean')
        self.assertEqual(self.employee_2.first, 'John')

    def test_email(self):
        # Regex expression for finding Sean.Cunniffe (some random number) @email.com
        self.assertRegex(self.employee_1.email, '^Sean.Cunniffe\d@email.com$')
        self.assertRegex(self.employee_2.email, '^John.Doe\d@email.com$')

    def test_apply_raise(self):
        self.employee_1.apply_raise()
        self.employee_2.apply_raise()

        self.assertEqual(self.employee_1.pay, 36000)
        self.assertEqual(self.employee_2.pay, 42000)

    def test_monthly_schedule(self):
        # mocks the request.get from employee,
        # you can set the return values when called and record the args passed to it
        # basically mocked_get == request.get in employee class
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            schedule = self.employee_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Cunniffe/May')
            self.assertEqual(schedule, 'Success!')

            mocked_get.return_value.ok = False

            schedule = self.employee_2.monthly_schedule('OCT')
            mocked_get.assert_called_with('http://company.com/Doe/OCT')
            self.assertEqual(schedule, 'Bad Response!')
