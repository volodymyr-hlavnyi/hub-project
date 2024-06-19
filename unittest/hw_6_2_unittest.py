import unittest
from hw.hw_6 import hw_62, hw_63


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):
    def test_hw6_2(self):
        output = hw_62(7)
        expected_output = (
            'First 7 Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8'
        )
        self.assertEqual(output, expected_output)

    def test_hw6_3(self):
        output = hw_63(17)
        expected_output = 'Number 17 is prime.'
        self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
