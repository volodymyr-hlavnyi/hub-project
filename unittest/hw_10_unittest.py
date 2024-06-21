import unittest
from hw.hw_10 import hw10_1, hw10_2, hw10_3


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw10_1(self):
        output = hw10_1('Hello, world!')
        expected_output = 'Hll, wrld!'
        self.assertEqual(output, expected_output)

    def test_hw10_2(self):
        output = hw10_2('Hello')
        expected_output = "Symbols l repeat."
        self.assertEqual(output, expected_output)

        output = hw10_2('Helloo')
        expected_output = "Symbols l and o repeat."
        self.assertEqual(output, expected_output)

    def test_hw10_3(self):
        output = hw10_3('Python', 10)
        expected_output = '  Python  '
        self.assertEqual(output, expected_output)

        output = hw10_3('Python', 11)
        expected_output = '     Python'
        self.assertEqual(output, expected_output)

        output = hw10_3('Python', 12)
        expected_output = '   Python   '
        self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
