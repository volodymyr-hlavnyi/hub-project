import unittest
from hw.hw_21 import count_words, print_fr_word, hw21_2,


class TestHomeworkFunction(unittest.TestCase):

    def test_hw21_1(self):
        self.assertEqual(count_words("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est."),
                         {'Lorem': 1, 'ipsum': 1, 'dolor': 1, 'sit': 1, 'amet,': 1, 'consectetur': 1, 'adipiscing': 1,
                          'elit.': 1, 'Sed': 1, 'sed': 1, 'lacinia': 1, 'est.': 1})

        self.assertEqual(
            count_words("Lorem Lorem ipsum dolor sit amet, sed consectetur adipiscing elit. Sed sed lacinia est."),
            {'Lorem': 2, 'ipsum': 1, 'dolor': 1, 'sit': 1, 'amet,': 1, 'consectetur': 1, 'adipiscing': 1,
             'elit.': 1, 'Sed': 1, 'sed': 2, 'lacinia': 1, 'est.': 1})

    def test_hw_21_2(self):
        self.assertEqual(hw21_2(),
                         (['Alice', 25, 'New York'],
                          ['Bob', 30, 'London'],
                          ['Carol', 35, 'Paris'])
                         )


if __name__ == '__main__':
    unittest.main()
