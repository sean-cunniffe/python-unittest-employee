# Created By SEAN CUNNIFFE on 14/01/2021
import unittest
from unittest import TestCase
import SimpleFunctions


# Import TestCase for testing
class Test(TestCase):

    def test_add(self):
        self.assertEqual(SimpleFunctions.add(10, 5), 15)
        self.assertEqual(SimpleFunctions.add(1, 5), 6)
        self.assertEqual(SimpleFunctions.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(SimpleFunctions.subtract(10, 5), 5)
        self.assertEqual(SimpleFunctions.subtract(5, 5), 0)
        self.assertEqual(SimpleFunctions.subtract(1, 5), -4)

    def test_multiplication(self):
        self.assertEqual(SimpleFunctions.multiplication(5, 5), 25)
        self.assertEqual(SimpleFunctions.multiplication(-1, 5), -5)
        self.assertEqual(SimpleFunctions.multiplication(0, 5), 0)

    def test_division(self):
        self.assertEqual(SimpleFunctions.division(5, 5), 1)
        self.assertEqual(SimpleFunctions.division(-5, 5), -1)
        self.assertEqual(SimpleFunctions.division(5, -10), -0.5)
        self.assertEqual(SimpleFunctions.division(5, 2), 2.5)
        self.assertEqual(SimpleFunctions.division(5, 5), 1)

        # Next two tests are the same just written differently

        self.assertRaises(ValueError, SimpleFunctions.division, 5, 0)

        with self.assertRaises(ValueError):
            SimpleFunctions.division(0, 0)


# If this class is ran directly it will run all of our tests

if __name__ == '__main__':
    unittest.main()
