import unittest
from p18 import *
class p18TestCase(unittest.TestCase):
      def test_ana1(self):
         try:  
            self.assertEqual(chk_anagram("google"),"anagram")
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
   
      def test_ana2(self):
         try:  
            self.assertEqual(chk_anagram("goggle"),"anagram")
            print(["success"])
         except Exception as e:
            print("not anagram")
            print("Execption is:",e)
if __name__=="__main__":
   unittest.main()
