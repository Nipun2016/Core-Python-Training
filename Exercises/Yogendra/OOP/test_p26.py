import unittest
from p6 import *
class p6TestCase(unittest.TestCase):
      def test_obj1(self):
         try:  
            sq1=Square()
            self.assertTrue(sq1.get_square(),1)
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
      
      def test_obj2(self):
         try:  
            sq1=Square()
            sq1=Square()
            sq1=Square()
            self.assertTrue(sq1.get_square(),3)
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
if __name__=="__main__":
     unittest.main()
