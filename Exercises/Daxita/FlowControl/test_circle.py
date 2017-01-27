import unittest
from circle import Circle

class CircleTestCase(unittest.TestCase):
    def test_area(self):
    	c=Circle(2)
    	self.assertEqual(c.area(),12.566370614359172)

    def test_perimeter(self):
    	c=Circle(2)
    	self.assertEqual(c.parimeter(),12.566370614359172)
if __name__=="__main__":
	unittest.main()