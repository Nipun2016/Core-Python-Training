import unittest
from str10 import *
class str10TestCase(unittest.TestCase):
      def test_count_string1(self):
         try:  
            self.assertEqual(count_str("i am yogi katewa katewa yogi katewa i am"),[('am', 2), ('i', 2), ('katewa', 3), ('yogi',2)])
            print("success")
         except Exception as e:
            print("Execption is:",e)
   
      def test_count_string2(self):
         try:
           self.assertEqual(count_str("this is yogendra katewa katewa"),[('is', 1), ('katewa', 2), ('this', 1), ('yogendra', 1)])
           print("success")
         except Exception as e:
           print("Exception is: ",e)

      def test_count_string3(self):
         try:
           self.assertTrue(count_str(""))
         except Exception as e:
           print("String cannot be remain blank: ")
           print("Exception is: ",e)
    

if __name__=="__main__":
   unittest.main()
