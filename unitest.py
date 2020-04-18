import unittest
from testing_hw17 import fin


class NameTestCase(unittest.TestCase):

    def test_name_model(self):
        car_model = fin('Mecedes', 'E-Class')
        self.assertEqual(car_model, 'Mercedes', 'E-Class')

unittest.main()
