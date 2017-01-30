import unittest
from polygon import Square, Rectangle, Triangle

class P4TestCase(unittest.TestCase):
    def test_square(self):
        obj = Square(4,[1,1,1,1])
        self.assertEqual(obj.get_area(),1)

    def test_rectange(self):
        obj = Rectangle(4,[1,2,1,2])
        self.assertEqual(obj.get_area(),2)

    def test_triangle(self):
        obj = Triangle(3,[4,5,6])
        self.assertEqual(obj.get_area(),9.921567416492215)

if __name__ == "__main__":
    unittest.main()
