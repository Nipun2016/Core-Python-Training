import unittest
from p6 import test_check

class P6TestCase(unittest.TestCase):
    def test_check_true(self):
        self.assertIsInstance(test_check([1,2,3,4],[1,2,3,4]),list)

if __name__ == "__main__":
    unittest.main()
