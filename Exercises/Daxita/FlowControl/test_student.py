import unittest
from student import student

class StudentTestCase(unittest.TestCase):
    def test_print_student(self):
        obj = student([1, 'raj'])
        self.assertEqual(obj.print(),[[1, 'raj']])

if __name__ == "__main__":
    unittest.main()