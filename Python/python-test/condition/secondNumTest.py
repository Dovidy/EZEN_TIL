import unittest
from secondNum import second_bigger_num

class secondNumTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(second_bigger_num(1, 2, 3), 2)

    def test_2(self):
        self.assertEqual(second_bigger_num(1, 3, 2), 2)

    def test_3(self):
        self.assertEqual(second_bigger_num(2, 1, 3), 2)

    def test_4(self):
        self.assertEqual(second_bigger_num(2, 3, 1), 2)

    def test_5(self):
        self.assertEqual(second_bigger_num(3, 1, 2), 2)

    def test_6(self):
        self.assertEqual(second_bigger_num(3, 2, 1), 2)

if __name__ == '__main__':
    unittest.main()