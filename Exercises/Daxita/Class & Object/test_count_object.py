import unittest
from count_object import count

class CountTestCase(unittest.TestCase):
	def test_count_object(self):
		c=count()
		self.assertEqual(count.counter,1)
if __name__=="__main__":
	unittest.main()