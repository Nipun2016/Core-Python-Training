import unittest    
from p3 import *
class p3TestCase(unittest.TestCase):
      def test_str1(self):
         try:  
            lst1=[]
            lst1=[-2,-1,1,2,3]
            #myc.area()
            self.assertTrue(subset(lst1,0),)
         except Exception as e:
            print("Execption is:",e)
   
      def test_str2(self):
         try:  
            lst1=[]
            lst1=[-2,-1,0,1,2]
            #myc.area()
            self.assertTrue(subset(lst1,0))
         except Exception as e:
            print("Execption is:",e)
      
      def test_str3(self):
         try:  
            lst1=[]
            lst1=[0,1,2,3,4,5]
            #myc.area()
            self.assertTrue(subset(lst1,0))
         except Exception as e:
            print("Execption is:",e)
      
            
if __name__=="__main__":
   unittest.main()
