import unittest
from stack import Stack

class StackTestCase(unittest.TestCase):
    def test_stack_push(self):
    	s=Stack(3)
    	self.assertEqual(s.push(3),1)

    def test_stack_pop(self):
    	s=Stack(3)
    	s.push(3)
    	self.assertEqual(s.pop(),3)

    def test_stack_none(self):
    	s=Stack(3)
    	self.assertEqual(s.pop(),"Stack Empty!!!!")
if __name__=="__main__":
	unittest.main()