import unittest
from hw.hw_16 import hw16_1, hw16_2


class TestHomeworkFunction(unittest.TestCase):

    def test_hw16_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(hw16_1(matrix), 45)

    def test_hw16_2(self):
        numbers = [5, 2, 8, 1, 3]
        self.assertEqual(hw16_2(numbers), [8, 5, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
