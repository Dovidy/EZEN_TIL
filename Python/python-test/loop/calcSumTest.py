import unittest
from calcSum import calc_sum

class alarmTest(unittest.TestCase):
    def test_a_b_sum(self):
        user_input = [
            '1, 2',
            '2, 3',
            '3, 4'
        ]

        right_ans = [
            '0: 1 + 2 = 3',
            '1: 2 + 3 = 5',
            '2: 3 + 4 = 7'
        ]

        with patch('builtins.input', side_effect=user_input):
            ans = calc_sum(3)

        self.assertEqual(ans, right_ans)

if __name__ == '__main__':
    unittest.main()