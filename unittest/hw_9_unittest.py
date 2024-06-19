import unittest
from hw.hw_9 import hw9_1, hw9_2


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw9_1(self):
        output = hw9_1('The quick brown fox jumps over the lazy dog')
        expected_output = 'String is pangram.'
        self.assertEqual(output, expected_output)

    def test_hw9_2(self):
        output = hw9_2('Hello World')
        expected_output = 'Number of vowels: 3\nNumber of consonants: 7'
        self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
