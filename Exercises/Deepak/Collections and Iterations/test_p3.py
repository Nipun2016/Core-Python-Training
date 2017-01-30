import unittest
from p3 import find_even_number

class P1TestCase(unittest.TestCase):
    def test_find_even(self):
        self.assertEqual(find_even_number([1,2,3,4,5,6]),[2,4,6])

if __name__ == "__main__":
    unittest.main()
