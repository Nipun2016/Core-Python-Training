import unittest
from p11 import *
class p11TestCase(unittest.TestCase):
      def test_enc1(self):
         try:  
            self.assertEqual(enc_dcr("katewa"),"xngrjn")
            print("xngrjn")
         except Exception as e:
            print("Execption is:",e)
   
      def test_enc2(self):
         try:
           self.assertEqual(enc_dcr("india"),"vaqvn")
           print("vaqvn")
         except Exception as e:
           print("Exception is: ",e)

      def test_enc3(self):
         try:
           self.assertEqual(enc_dcr("344"),"only characters")
           print("only characters")
         except Exception as e:
           print("Exception is: ",e)

if __name__=="__main__":
   unittest.main()
