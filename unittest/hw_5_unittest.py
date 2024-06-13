import unittest
from hw.hw_5 import hw5_1_1, hw5_1_2, hw5_2


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw5_1_1(self):
        output = hw5_1_1(5, 2, 7)
        expected_output = (
            'Numbers in ascending order: 2, 5, 7'
        )
        self.assertEqual(output, expected_output)

    def test_hw5_1_2(self):
        output = hw5_1_2(5, 2, 7)
        expected_output = (
            'Numbers in ascending order: 2, 5, 7'
        )
        self.assertEqual(output, expected_output)

    def test_hw5_2(self):
        output = hw5_2(2024)
        expected_output = 'The year is a leap year.'
        self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
