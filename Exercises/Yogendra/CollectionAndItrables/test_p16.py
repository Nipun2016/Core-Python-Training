import unittest
from p16 import *
class p16TestCase(unittest.TestCase):
      def test_tupp1(self):
         try:  
            self.assertEqual(unpack((("i","am","katewa"),("1","8","94"))),["i","am","katewa"],["1","8","94"])
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
   
      
if __name__=="__main__":
   unittest.main()
