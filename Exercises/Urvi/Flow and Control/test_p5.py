import unittest
from p5 import is_common

class P5TestCase(unittest.TestCase):

    def test_is_common(self):
        self.assertTrue(is_common([11,22,33,44],[22,77,88,99]))


if __name__ == "__main__":
    unittest.main()
