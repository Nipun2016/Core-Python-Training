import unittest
from swiden_msg import swiden

class SwidenMsgTestCase(unittest.TestCase):
    def test_swiden(self):
        self.assertEqual(swiden("happy new year"),['gott', 'nytt', 'år'])
if __name__=="__main__":
	unittest.main()