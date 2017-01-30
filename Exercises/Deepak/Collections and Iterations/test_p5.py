import unittest
from p5 import valid_input, check_brackets

class P5TestCase(unittest.TestCase):
    def test_valid_input_string(self):
        self.assertFalse(valid_input("Happy"))

    def test_valid_input_digit(self):
        self.assertFalse(valid_input("123"))

    def test_valid_input_None(self):
        self.assertFalse(valid_input("None"))

    def test_check_brackets(self):
        self.assertEqual(check_brackets("[][]"),"Ok")

if __name__ == "__main__":
    unittest.main()
