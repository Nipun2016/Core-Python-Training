import unittest
from str6 import *
class str6TestCase(unittest.TestCase):
      def test_chk_lst(self):
         try:  
            self.assertTrue(lst_cmn([1,2,3,4,5,6,7,8],[2,3,4,9,11]))
            print("success")
         except Exception as e:
            print("Execption is:",e)
   
      def test_lst_new(self):
         try:
           self.assertTrue(lst_cmn([1,2,3,4,5,6,7,8],[10,11,12,13]))
           print("success")
         except Exception as e:
           print("List are not same: ")
           print("Exception is: ",e)

      def test_lst_emp_frst(self):
         try:
           self.assertTrue(lst_cmn([],[10,11,12,13]))
           print("success")
         except Exception as e:
           print("List 1 is empty: ")
           print("Exception is: ",e)

      def test_lst_emp_lst(self):
         try:
           self.assertTrue(lst_cmn([1,2,3,4,5,6,7,8],[]))
           print("success")
         except Exception as e:
           print("List 2 is empty: ")
           print("Exception is: ",e)

      def test_lst_emp(self):
         try:
           self.assertTrue(lst_cmn([],[]))
           print("success")
         except Exception as e:
           print("List cannot be empty:")
           print("Exception is: ",e)

if __name__=="__main__":
   unittest.main()
