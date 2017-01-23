import unittest
from gen_range import gen

class GenRangeTestCase(unittest.TestCase):
    def test_gen_range(self):
    	g=gen(3)
    	for i in range(0,3):
    		#print(next(g))
        	self.assertEqual(next(g),i)

if __name__=="__main__":
	unittest.main()