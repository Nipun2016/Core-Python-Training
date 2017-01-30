import unittest
from p3 import check

class P3TestCase(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check("deepak"))

if __name__ == "__main__":
    unittest.main()
