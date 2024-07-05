import unittest
from hw.hw_20 import merge_digits, count_unique_chars


class TestHomeworkFunction(unittest.TestCase):

    def test_hw20_1(self):
        self.assertEqual(merge_digits({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}),
                         {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]})

    def test_hw20_2(self):
        self.assertEqual(count_unique_chars('Hello, World!'), 10)
        self.assertEqual(count_unique_chars('hello'), 4)


if __name__ == '__main__':
    unittest.main()
