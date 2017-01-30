import unittest
from str8 import *
class str8TestCase(unittest.TestCase):
      def test_chk_prime_2(self):
         try:  
            self.assertTrue(is_prime(2))
            print("sucess")
         except Exception as e:
            print("Execption is:",e)
   
      def test_chk_prime_3(self):
         try:
           self.assertTrue(is_prime(3))
           print("sucess")
         except Exception as e:
           print("Exception is: ",e)

      def test_chk_prime4(self):
         try:
           self.assertTrue(is_prime(4))
         except Exception as e:
           print("4 is not prime: ")
           print("Exception is: ",e)

    

if __name__=="__main__":
   unittest.main()
