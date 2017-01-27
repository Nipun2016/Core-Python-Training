import unittest
from even_no import even_num

class EvenTestCase(unittest.TestCase):
    def test_even(self):
        self.assertEqual(even_num([2,5,67,43,34]),[2,34])

if __name__ == "__main__":
    unittest.main()