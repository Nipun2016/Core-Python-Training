import unittest
from str9 import *
class str9TestCase(unittest.TestCase):
      def test_chk_pangram1(self):
         try:  
            self.assertEqual(chk_panagram("1i am katewa yogendra"),"!Error---wrong input")
            print("!Error---wrong input")
         except Exception as e:
            print("Execption is:",e)
   
      def test_chk_pangram2(self):
         try:
           self.assertEqual(chk_panagram("The quick brown fox jumps over the lazy dog"),"pangram")
           print("pangram")
         except Exception as e:
           print("Exception is: ",e)

      def test_chk_pangram3(self):
         try:
           self.assertEqual(chk_panagram("india beats england"),"not")
           print("not panagram")
         except Exception as e:
           print("Exception is: ",e)

      def test_chk_pangram4(self):
         try:
           self.assertEqual(chk_panagram(""),"not")
           print("not panagram")
         except Exception as e:
           print("Exception is: ",e)

if __name__=="__main__":
   unittest.main()
