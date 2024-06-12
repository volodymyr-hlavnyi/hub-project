import unittest
from math import pi
from hw.hw_3 import hw3_1, hw3_2, hw3_3


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw3_1(self):
        output = hw3_1(5, 2)
        expected_output = (
            'Сумма: 7\n'
            'Разность: 3\n'
            'Произведение: 10\n'
            'Частное: 2.5\n'
            'Остаток от деления: 1\n'
            'Первое число в степени второго числа: 25'
        )
        self.assertEqual(output, expected_output)

    def test_hw3_2(self):
        output = hw3_2(4.5)
        expected_output = (
            f'Длина окружности: {2 * pi * 4.5}\n'
            f'Площадь окружности: {pi * 4.5 ** 2}'
        )
        self.assertEqual(output, expected_output)

    def test_hw3_3(self):
        output = hw3_3(2, 3, 5, 7)
        expected_output = 'Расстояние между точками: 5.0'
        self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
