import unittest
from p8 import KinderGarten

class P7TestCase(unittest.TestCase):
    def test_calculate_data(self):
        obj = KinderGarten("Alice")
        self.assertEqual(obj.calculate_data(),['Violets', 'Radishes', 'Violets', 'Radishes'])

    def test_calculate_Flase_string(self):
        obj = KinderGarten("urvi")
        self.assertEqual(obj.calculate_data(),"Name not found....")

    def test_calculate_Flase_number(self):
        obj = KinderGarten("123")
        self.assertEqual(obj.calculate_data(),"Name not found....")

if __name__ == "__main__":
    unittest.main()
