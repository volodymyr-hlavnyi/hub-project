import unittest
from hw.hw_4 import hw4_2_print


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw4_2(self):
        output = hw4_2_print(True, False)
        expected_output = (
            'Результат логического И: False\n'
            'Результат логического ИЛИ: True\n'
            'Результат логического НЕ (для первого значения): False\n'
            'Результат логического НЕ (для второго значения): True\n'
            'Результат сравнения на равенство: False\n'
            'Результат сравнения на неравенство: True'
        )
        self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
