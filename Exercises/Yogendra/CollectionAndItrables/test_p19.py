import unittest
from p19 import *
class p19TestCase(unittest.TestCase):
      def test_cal1(self):
         try:  
            self.assertEqual(num_cal(15),[6,9,10,12])
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
   
      def test_cal2(self):
         try:  
            self.assertEqual(num_cal(0),[])
            print(["success"])
         except Exception as e:
            print("Execption is:",e)

      def test_cal3(self):
         try:  
            self.assertEqual(num_cal("ten"),[6,9])
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
            print("cannot pass a string")
if __name__=="__main__":
   unittest.main()
