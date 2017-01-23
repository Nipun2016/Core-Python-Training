import unittest
from p4 import reverselist

class P4TestCase(unittest.TestCase):
    def test_check(self):
        self.assertEqual(reverselist(["deepak","urvi"]),["irvu","keepad"])

if __name__ == "__main__":
    unittest.main()
