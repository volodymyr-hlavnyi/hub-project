import unittest
import io
import sys
from contextlib import redirect_stdout
from hw.hw_13 import hw13_1, hw13_2


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw13_1(self):
        output = hw13_1(3, 4)
        expected_output = (7, 12)
        self.assertEqual(output, expected_output)

    def test_hw13_2(self):
        output = hw13_2([3, 7, 2, 9, 1, 5])
        expected_output = (27, 1, 9)
        self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
