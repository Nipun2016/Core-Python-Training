import unittest
from p5 import Student

class P2TestCase(unittest.TestCase):
    def test_print_data(self):
        obj = Student([1, 'dac'])
        self.assertEqual(obj.print_data(),[[1, 'dac']])

if __name__ == "__main__":
    unittest.main()
