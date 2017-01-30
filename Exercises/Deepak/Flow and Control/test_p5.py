import unittest
from p5 import fun

class P5TestCase(unittest.TestCase):
    def test_check(self):
        self.assertTrue(fun([1,2,3,4],[11,22,3,44]))

if __name__ == "__main__":
    unittest.main()
