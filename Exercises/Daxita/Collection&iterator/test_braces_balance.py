import unittest
from braces_balance import balance,valid_input

class BracesTestCase(unittest.TestCase):
	def test_balance(self):
		self.assertEqual(balance("[][]"),"OK")

	def test_valid_input_string(self):
		self.assertFalse(valid_input("Happy"))

	def test_valid_input_digit(self):
		self.assertFalse(valid_input("123"))

	def test_valid_input_None(self):
		self.assertFalse(valid_input("None"))

if __name__ == "__main__":
    unittest.main()