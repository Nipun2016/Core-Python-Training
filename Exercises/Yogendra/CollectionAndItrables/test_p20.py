import unittest
from p20 import *
class p20TestCase(unittest.TestCase):
      def test_cal1(self):
         try:
            y=yrange(2)  
            self.assertEqual(y.__next__(),0)
            print("success")
            self.assertEqual(y.__next__(),1)
            print("success")
            self.assertEqual(y.__next__(),2)
         except Exception as e:
            print("Execption is:",e)
      
      def test_cal2(self):
         try:
            y=yrange("hg")  
            self.assertEqual(y.__next__(),0)
            print("success")
            self.assertEqual(y.__next__(),1)
            print("success")
         except Exception as e:
            print("Execption is:",e)
if __name__=="__main__":
   unittest.main()
