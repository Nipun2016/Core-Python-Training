import unittest
from pangram import panagram

class PanagramTestCase(unittest.TestCase):
    def test_panagram_True(self):
        self.assertEqual(panagram("abcdefghijklmnopqrstuvwxyzjhdwg"),True)
    def test_panagram_False(self):
        self.assertEqual(panagram("DFRE$%^4 EFv"),False)

if __name__ == "__main__":
    unittest.main()