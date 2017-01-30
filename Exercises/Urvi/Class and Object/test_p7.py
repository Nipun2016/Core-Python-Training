import unittest
from p7 import Stack

class P7TestCase(unittest.TestCase):
    def test_push_data(self):
        obj = Stack(4)
        obj.push(1)
        obj.push(5)
        self.assertEqual(obj.push(6),3)

    def test_pop_data(self):
        obj = Stack(4)
        obj.push(1)
        obj.push(5)
        self.assertEqual(obj.pop(),5)

    def test_size(self):
        obj = Stack(4)
        obj.push(1)
        obj.push(5)
        self.assertEqual(obj.stack_size(),2)

if __name__ == "__main__":
    unittest.main()
