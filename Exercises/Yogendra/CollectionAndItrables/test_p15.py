import unittest
from p15 import *
class p15TestCase(unittest.TestCase):
      def test_brac1(self):
         try:  
            self.assertEqual(square("[][][][][]["),"not closed properly:")
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
   
      def test_brac2(self):
         try:  
            self.assertEqual(square("[][][[]][][[]][[]]"),"right closing:")
            print(["success"])
         except Exception as e:
            print("Execption is:",e)

      def test_brac3(self):
         try:  
            self.assertEqual(square("[][][[{}]][][[]][[()]]"),"only square brackets:")
            print(["success"])
         except Exception as e:
            print("Execption is:",e)

if __name__=="__main__":
   unittest.main()
