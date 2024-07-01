import unittest
from hw.hw_17 import hw17_1, hw17_2


class TestHomeworkFunction(unittest.TestCase):

    def test_hw17_1(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(hw17_1(numbers), [2, 1, 6, 2, 10])

    def test_hw17_2(self):
        self.assertEqual(hw17_2(1, 2, 3, 4, 5), 15)


if __name__ == '__main__':
    unittest.main()
