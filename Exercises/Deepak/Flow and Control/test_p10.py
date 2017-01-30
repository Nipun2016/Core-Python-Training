import unittest
from p10 import count_words, valid_data

class P10TestCase(unittest.TestCase):
    def test_count_words(self):
        self.assertIsInstance(count_words("deepak deepak deepak chaudhary"),dict)

    def test_valid_data_true(self):
        self.assertEqual(valid_data(['deepak', 'deepak', 'deepak', 'chaudhary']),['deepak', 'deepak', 'deepak', 'chaudhary'])

    def test_valid_data_False(self):
        self.assertFalse(valid_data(['deepak', 9]))

    def test_valid_data_None(self):
        self.assertFalse(valid_data(None))

if __name__ == "__main__":
    unittest.main()
