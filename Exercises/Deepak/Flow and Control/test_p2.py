import unittest
from p2 import changeChar, formate_data

class P2TestCase(unittest.TestCase):
    def test_change_Char(self):
        self.assertEqual(changeChar(['d','e','e','p','a','k','d'],"d"), "deepak$")

    def test_change_number(self):
        self.assertFalse(formate_data(123))

    def test_changeChar_None(self):
        self.assertFalse(formate_data(None))

    def test_changeChar_Value(self):
        self.assertEqual(formate_data("Deepakd"),(['D','e','e','p','a','k','d'],"D"))

if __name__ == "__main__":
    unittest.main()
