import unittest
from p5 import *
class p5TestCase(unittest.TestCase):
      def test_stud1(self):
         try:  
            stud=Student(1,"yogendra")
            self.assertEqual(stud.get_details(),(1,"yogendra"))
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
   
      def test_stud2(self):
         try:  
            #lst=[]
            stud=Student(1,"yogendra")
            self.assertEqual(stud.get_details(),(2,"katewa"))
            print(["success"])
         except Exception as e:
            print("Execption is:",e)

      def test_stud3(self):
         try:  
            #lst=[]
            
            self.assertEqual(sort([(1,"yogendra"),(3,"katewa"),(2,"here")]),[(1, 'yogendra'), (2, 'here'), (3, 'katewa')])
            print(["success"])
         except Exception as e:
            print("Execption is:",e)      
if __name__=="__main__":
   unittest.main()
