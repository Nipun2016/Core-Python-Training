import unittest
from p7 import *
class p7TestCase(unittest.TestCase):
      def test_stk1(self):
         try:  
            stk1=Stack(1,5,[],"katewa")
            stk2=Stack(1,5,["i","am","yogendra","from","navsari"],"yogendra")
            self.assertEqual(stk1.stack_update(),["katewa"])
            print(["success"])
            self.assertEqual(stk2.stack_update(),["yogendra"])
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
      
      
      def test_stk2(self):
         try:  
            stk1=Stack(0,5,[])
            stk2=Stack(1,5,["i","am","yogendra","from","navsari"],"yogendra")
            self.assertTrue(stk1.stack_update())
            print(["success"])
            self.assertEqual(stk2.stack_update(),["yogendra"])
            print(["success"])
         except Exception as e:
            print("Execption is:",e)	
if __name__=="__main__":
     unittest.main()
