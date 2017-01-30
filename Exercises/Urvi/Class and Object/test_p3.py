import unittest
from p3 import CalculateSum

class P2TestCase(unittest.TestCase):
    def test_sum_true(self):
        obj = CalculateSum([5,5,-10])
        self.assertEqual(obj.getAnswer(),[[5,5,-10]])

    def test_sum_false(self):
        obj = CalculateSum([1,2,3])
        self.assertEqual(obj.getAnswer(),[])

if __name__ == "__main__":
    unittest.main()
