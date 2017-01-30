import unittest
from str5 import *
class str5TestCase(unittest.TestCase):
      def test_chk_lst(self):
         try:  
            self.assertTrue(chk_lst([1,2,3,4,5,6,7,8],[2,3,4,9,11]))
            print("success")
         except Exception as e:
            print("Execption is:",e)
   
      def test_lst_new(self):
         try:
           self.assertTrue(chk_lst([1,2,3,4,5,6,7,8],[10,11,12,13]))
           print("success")
         except Exception as e:
           print("List are not same: ",e)
           print("Exception is: ",e)

      def test_lst_emp_frst(self):
         try:
           self.assertTrue(chk_lst([],[10,11,12,13]))
           print("success")
         except Exception as e:
           print("List 1 is empty: ",e)
           print("Exception is: ",e)

      def test_lst_emp_lst(self):
         try:
           self.assertTrue(chk_lst([1,2,3,4,5,6,7,8],[]))
           print("success")
         except Exception as e:
           print("List 2 is empty: ",e)
           print("Exception is: ",e)

      def test_lst_emp(self):
         try:
           self.assertTrue(chk_lst([],[]))
           print("success")
         except Exception as e:
           print("List cannot be empty: ",e)
           print("Exception is: ",e)

if __name__=="__main__":
   unittest.main()
