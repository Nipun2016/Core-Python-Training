import unittest
from p12 import *
class p12TestCase(unittest.TestCase):
      def test_len1(self):
         try:  
            self.assertTrue(wrd_len(["katewa"]))
            print("success")
         except Exception as e:
            print("Execption is:",e)
   
      def test_len2(self):
         try:  
            self.assertTrue(wrd_len(["yogendra"]))
            print("success")
         except Exception as e:
            print("Execption is:",e)
     
if __name__=="__main__":
   unittest.main()
