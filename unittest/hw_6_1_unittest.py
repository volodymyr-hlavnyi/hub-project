#

import unittest
from unittest.mock import patch
from hw.hw_6 import guess_number, hw_61


class TestHW6(unittest.TestCase):
    def test_guess_number(self):
        self.assertEqual(
            guess_number(50, 50),
            'Congratulation! You guessed the number 50.')
        self.assertEqual(
            guess_number(40, 50),
            'The number is greater.')
        self.assertEqual(
            guess_number(60, 50),
            'The number is less.')

    @patch('hw.hw_6.random.randint')
    @patch('builtins.input')
    def test_hw_61(self, mock_input, mock_randint):
        mock_randint.return_value = 50
        mock_input.side_effect = [60, 40, 50]
        with patch('builtins.print') as mock_print:
            hw_61()
            mock_print.assert_any_call('The number is less.')
            mock_print.assert_any_call('The number is greater.')
            mock_print.assert_called_with('Congratulation! You guessed the number 50.')


if __name__ == '__main__':
    unittest.main()
