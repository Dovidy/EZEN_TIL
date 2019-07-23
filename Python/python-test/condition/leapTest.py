import unittest
from leap import isLeap 

class leapTest(unittest.TestCase):
    def test_2012(self):
        self.assertTrue(isLeap(2012))
    
    def test_1900(self):
        self.assertFalse(isLeap(1900))

    def test_2000(self):
        self.assertTrue(isLeap(2000))
        
if __name__ == '__main__':
    unittest.main()