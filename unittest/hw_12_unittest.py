import unittest
import io
import sys
from contextlib import redirect_stdout
from hw.hw_12 import hw12_1, hw12_2


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw12_1_1(self):
        expected_output = "  1  2  3  4  5\n  2  4  6  8 10\n  3  6  9 12 15\n  4  8 12 16 20\n  5 10 15 20 25\n"
        f = io.StringIO()
        with redirect_stdout(f):
            hw12_1(5, '>')
        output = f.getvalue()
        self.assertEqual(output, expected_output)

    def test_hw12_1_2(self):
        expected_output = '1  2  3  4  5  \n2  4  6  8  10 \n3  6  9  12 15 \n4  8  12 16 20 \n5  10 15 20 25 \n'
        f = io.StringIO()
        with redirect_stdout(f):
            hw12_1(5, '<')
        output = f.getvalue()
        self.assertEqual(output, expected_output)

    def test_hw12_2(self):
        output = hw12_2('1 2 3 4 5', 'A B C D E')
        expected_output = "List of pairs of elements: [('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D'), ('5', 'E')]"
        self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
