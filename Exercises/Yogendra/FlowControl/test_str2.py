import unittest
from str2 import *
class str2TestCase(unittest.TestCase):
     def test_str_cal(self):
      try:  
         self.assertEqual(str_mul("katewak"), "katewa$")
         print("success")
      except Exception as e:
         print(e)
   
     def test_str_cal_rep(self):
      try:
           self.assertTrue(str_mul("katewa"))
      except Exception as e:
           print("!---first number is not repeating: ")
           print("Exception is: ",e)

     def test_str_cal_one(self):
      try:
           self.assertTrue(str_mul("k"))
      except Exception as e:
           print("!---first number is not repeating: ")
           print("Exception is: ",e)

     def test_str(self):
      try:
           self.assertTrue(str_mul(""))
      except Exception as e:
           print("!---Empty string: ")
           print("Exception is: ",e)

if __name__=="__main__":
    unittest.main()
