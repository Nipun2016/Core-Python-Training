import unittest
from p10 import count_words, valid_data

class P10TestCase(unittest.TestCase):
    def test_count_words(self):
        self.assertIsInstance(count_words("urvi urvi urvi kirtikumar patel "),dict)

    def test_valid_data_true(self):
        self.assertEqual(valid_data(['urvi', 'urvi', 'urvi', 'patel']),['urvi', 'urvi', 'urvi', 'urvi'])

    def test_valid_data_False(self):
        self.assertFalse(valid_data(['urvi', 9]))

    def test_valid_data_None(self):
        self.assertFalse(valid_data(None))

if __name__ == "__main__":
    unittest.main()
