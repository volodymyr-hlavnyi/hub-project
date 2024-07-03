import unittest
from hw.hw_18 import hw18_1, sum_digits


class TestHomeworkFunction(unittest.TestCase):

    def test_hw18_1(self):
        self.assertEqual(hw18_1(5), 120)
    def test_hw18_2(self):
        self.assertEqual(sum_digits([1, 2, 3, 4, 5]), 15)


if __name__ == '__main__':
    unittest.main()
