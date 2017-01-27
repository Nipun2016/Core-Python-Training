import unittest
from sum_zero import sum_zero

class PrintStrTestCase(unittest.TestCase):
    def test_sum_zero(self):
    	S=sum_zero()
    	self.assertEqual(S.compute([2,3,4,6,0,-1,-6]),[[2, 4, -6], [6, 0, -6]])
if __name__=="__main__":
	unittest.main()