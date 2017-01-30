import unittest
from str3 import *
class str3TestCase(unittest.TestCase):
      def test_dict(self):
         try:  
            self.assertFalse(key_check("sape","circle"))
            print("key is already exist")
         except Exception as e:
            print("Execption is:",e)
   
      def test_str_new(self):
         try:
           self.assertTrue(key_check("katewa","katewa"))
           print("success")
         except Exception as e:
           print("Exception is: ",e)

if __name__=="__main__":
   unittest.main()
