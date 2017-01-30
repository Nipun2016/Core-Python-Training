import unittest
from p13 import *
class p13TestCase(unittest.TestCase):
      def test_even1(self):
         try:  
            self.assertEqual(eve_only(2),[])
            print("success")
         except Exception as e:
            print("Execption is:",e)
   
      def test_even2(self):
         try:
           self.assertEqual(eve_only(3),[2])
           print("sucess")
         except Exception as e:
           print("Exception is: ",e)
    
      def test_even3(self):
         try:
           self.assertEqual(eve_only("a"),[])
           print("sucess")
         except Exception as e:
           print("Exception is: ",e)
      
if __name__=="__main__":
   unittest.main()
