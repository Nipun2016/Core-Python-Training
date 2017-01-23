import unittest
from p2 import Circle

class P2TestCase(unittest.TestCase):
    def test_area(self):
        obj = Circle(2)
        self.assertEqual(obj.getArea(),12.566370614359172)

    def test_perimeter(self):
        obj = Circle(2)
        self.assertEqual(obj.getPerimeter(),12.566370614359172)

if __name__ == "__main__":
    unittest.main()
