import unittest
from p9 import ispanagram

class P9TestCase(unittest.TestCase):
    def test_panagram_True(self):
        self.assertEqual(ispanagram("qwertyuioplkjhgfdsazxcvbnm"),True)

    def test_panagram_False(self):
        self.assertEqual(ispanagram("Deepak81048@gmail.com"),False)

if __name__ == "__main__":
    unittest.main()
