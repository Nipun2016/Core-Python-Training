import unittest
from str1 import *
class str1TestCase(unittest.TestCase):
     def test_str_cal(self):
      try:  
         self.assertEqual(str_mul("katewa",2,4), "kakakaka")
         print("success")
      except Exception as e:
         print(e)
   
     def test_str_cal_rep(self):
      try:
           self.assertEqual(str_mul("katewa",2,"abc"))
      except Exception as e:
           print("!---repeating number is not number: ")
           print("Exception is: ",e)
         
     def test_str_cal_char(self):
       try:
           self.assertFalse(str_mul("katewa","abc",4))
       except Exception as e:
           print("!----character position is not number")
           print("Execption is:",e)
     
     def test_str_cal_char_rep(self):
       try:
           self.assertFalse(str_mul("katewa","abc","bgf"))
       except Exception as e:
           print("!----character position and repeating is not number")
           print("Execption is:",e)
  
     def test_str_cal_char_none(self):
       try:
           self.assertFalse(str_mul("katewa",None,3))
       except Exception as e:
           print("!----character position cant be null")
           print("Execption is:",e)
   
     def test_str_cal_char_rep_none(self):
       try:
           self.assertFalse(str_mul("katewa",None,None))
       except Exception as e:
           print("!----character position and repeating number cant be null")
           print("Execption is:",e)
     def test_str_cal_rep_none(self):
       try:
           self.assertFalse(str_mul("katewa",2,None))
       except Exception as e:
           print("!----repeating number cant be null")
           print("Execption is:",e)
   
if __name__ == "__main__": 
     unittest.main()       
