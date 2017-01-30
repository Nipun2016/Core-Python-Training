import unittest
from str4 import *
class str4TestCase(unittest.TestCase):
      def test_lst(self):
         try:  
            self.assertTrue(lst([]))
            print("success")
         except Exception as e:
            print("List is empty")
            print("Execption is:",e)
   
      def test_lst_new(self):
         try:
           self.assertTrue(lst(["india","australia","England","Africa"]))
           print("success")
         except Exception as e:
           print("Exception is: ",e)

if __name__=="__main__":
   unittest.main()
