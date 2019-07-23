import unittest
from alarm import alarmBefore

class alarmTest(unittest.TestCase):
    def test_smaller_than_45(self):
        self.assertEqual(alarmBefore(7, 0), (6, 15))

    def test_hour_0(self):
        self.assertEqual(alarmBefore(0, 15), (23, 30))
    
    def test_bigger_than_45(self):
        self.assertEqual(alarmBefore(7, 45), (7, 0))

if __name__ == '__main__':
    unittest.main()
