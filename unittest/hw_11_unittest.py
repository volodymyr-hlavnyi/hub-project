import unittest
from hw.hw_11 import hw11_1_1, hw11_1_2, hw11_2


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw11_1_1(self):
        output = hw11_1_1('Alice', 25, 'London')
        expected_output = 'Hello, my name is Alice. I am 25 years old. I live in London.'
        self.assertEqual(output, expected_output)

        output = hw11_1_1('Bob', 35, 'Kiew')
        expected_output = 'Hello, my name is Bob. I am 35 years old. I live in Kiew.'
        self.assertEqual(output, expected_output)

    def test_hw11_1_2(self):
        output = hw11_1_2('Alice', 25, 'London')
        expected_output = 'Hello, my name is Alice. I am 25 years old. I live in London.'
        self.assertEqual(output, expected_output)

        output = hw11_1_1('Bob', 35, 'Kiew')
        expected_output = 'Hello, my name is Bob. I am 35 years old. I live in Kiew.'
        self.assertEqual(output, expected_output)

    def test_hw11_2(self):
        output = hw11_2(3.14159, 2.71828)
        expected_output = 'Sum: 5.86, Product: 8.54'
        self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
