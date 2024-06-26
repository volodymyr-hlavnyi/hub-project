import unittest
from unittest.mock import patch
from hw.hw_14 import hw14_1, hw14_2


# Define the test cases
class TestHomeworkFunctions(unittest.TestCase):

    def test_hw14_1(self):
        self.assertEqual(hw14_1('Programming is interesting and useful'), 'useful and interesting is Programming')

    def test_hw14_2(self):
        @patch('builtins.input', side_effect=['1', '2', 'Exit'])
        def test_hw14_2(self, mock_input):
            expected_output = ['1', '2']
            output = hw14_2()
            self.assertEqual(output, expected_output)


# Run the tests
if __name__ == "__main__":
    unittest.main()
