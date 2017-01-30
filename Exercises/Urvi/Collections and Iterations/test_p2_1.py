import unittest
from p2_1 import find_length, valid_input

class P1TestCase(unittest.TestCase):
    def test_find_length(self):
        self.assertEqual(find_length(['urvi','patel']),[4,5])

    def test_find_length_String(self):
        self.assertTrue(valid_input("ur"))

    def test_find_length_String_Number(self):
        self.assertFalse(valid_input(['urvi',8,"#$%"]))

    def test_find_length_None(self):
        self.assertFalse(valid_input(None))

if __name__ == "__main__":
    unittest.main()
