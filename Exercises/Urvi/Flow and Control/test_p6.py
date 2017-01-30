import unittest
from p6 import common_list

class P5TestCase(unittest.TestCase):

    def test_common_list(self):
        self.assertIsInstance(common_list([11,22,33,44],[22,77,88,99]),list)

    

    def test_common_list_ans(self):
        self.assertEqual(common_list([1,3,5,9],[3,6,9,12]),[3,9])
if __name__ == "__main__":
    unittest.main()
