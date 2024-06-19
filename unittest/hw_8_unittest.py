import unittest
from hw.hw_8 import hw8_1, hw8_2


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw8_1(self):
        output = hw8_1(12321)
        expected_output = 'The number is a palindrome.'
        self.assertEqual(output, expected_output)

    def test_hw8_2(self):
        output = hw8_2(153)
        expected_output = 'The number is an Armstrong number.'
        self.assertEqual(output, expected_output)

# Run the tests
if __name__ == "__main__":
    unittest.main()
