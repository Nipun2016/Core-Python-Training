import unittest
from kindergarten import kindergarten

class KindergartenTestCase(unittest.TestCase):
    def test_kindergarten(self):
    	s=kindergarten()
    	self.assertEqual(s.plants("Alice"),("Violets", "Radishes", "Violets", "Radishes"))

    def test_kindergarten1(self):
    	s=kindergarten()
    	self.assertEqual(s.plants("Bob"),('Clover', 'Grass', 'Clover', 'Clover'))

if __name__=="__main__":
	unittest.main()