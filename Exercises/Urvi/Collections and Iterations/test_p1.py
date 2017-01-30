import unittest
from p1 import convert, valid_input

class P1TestCase(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert("urvi"),['h','e','i','v',' '])

    def test_covert_number(self):
        self.assertFalse(valid_input(3))

    def test_covert_String(self):
        self.assertTrue(valid_input("urvi"))

    def test_covert_None(self):
        self.assertFalse(valid_input(None))

if __name__ == "__main__":
    unittest.main()
