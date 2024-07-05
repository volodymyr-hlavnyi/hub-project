import unittest
from hw.hw_20 import merge_digits, count_unique_chars, calculate_average_grade


class TestHomeworkFunction(unittest.TestCase):

    def test_hw20_1(self):
        self.assertEqual(merge_digits({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}),
                         {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]})

    def test_hw20_2(self):
        self.assertEqual(count_unique_chars('Hello, World!'), 10)
        self.assertEqual(count_unique_chars('hello'), 4)

    def test_hw20_3(self):
        a = {
            'Alice': [85, 90, 92],
            'Bob': [78, 80, 84],
            'Carol': [92, 88, 95]
        }
        a_result = {'Alice': 89.0, 'Bob': 80.66666666666667, 'Carol': 91.66666666666667}
        self.assertEqual(calculate_average_grade(a), a_result)
        b = {
            'Ivanov': [4, 5, 3, 4],
            'Petrov': [3, 4, 5, 5]
        }
        b_result = {'Ivanov': 4.0, 'Petrov': 4.25}
        self.assertEqual(calculate_average_grade(a), a_result)


if __name__ == '__main__':
    unittest.main()
