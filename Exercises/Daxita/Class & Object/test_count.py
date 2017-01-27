import unittest
from count import count_words, valid_data

class CountWordTestCase(unittest.TestCase):
    def test_count_words(self):
        self.assertIsInstance(count_words("ih ihbi iubniubu"),dict)

    def test_valid_data_False(self):
        self.assertFalse(valid_data(['jbggfrhjin', 10]))

    def test_valid_data_None(self):
        self.assertFalse(valid_data(None))

if __name__ == "__main__":
    unittest.main()