import unittest
from p5 import Student

class P2TestCase(unittest.TestCase):
    def test_print_data(self):
        obj = Student([1, 'uru'])
        self.assertEqual(obj.print_data(),[[1, 'uru']])

if __name__ == "__main__":
    unittest.main()
