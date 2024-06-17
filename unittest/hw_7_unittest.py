import unittest
from hw.hw_7 import hw_71, hw_72


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw7_1(self):
        output = hw_71(123)
        expected_output = '1111011'
        self.assertEqual(output, expected_output)

    def test_hw7_2(self):
        output = hw_72(-3.14)
        expected_output = -3
        self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
