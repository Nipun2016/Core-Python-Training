import unittest
from p4 import valid_input, convert_data

class P1TestCase(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(valid_input("Happy"),["Happy"])

    def test_convert_data(self):
        self.assertEqual(convert_data(['happy']),'gott')

    def test_valid_input_number(self):
        try:
            self.assertFalse(valid_input(123))
        except Exception as e:
            print ("Insert String Only...")

    def test_valid_input_none(self):
        try:
            self.assertFalse(valid_input(None))
        except Exception as e:
            print ("Insert String Only...")

if __name__ == "__main__":
    unittest.main()
