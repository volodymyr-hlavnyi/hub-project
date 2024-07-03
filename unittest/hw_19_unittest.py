import unittest
from hw.hw_19 import hw19_1, is_subset


class TestHomeworkFunction(unittest.TestCase):

    def test_hw19_1(self):
        list_of_words = ['cat', 'dog', 'tac', 'god', 'act']
        self.assertEqual(hw19_1(list_of_words), [['cat', 'tac', 'act'], ['dog', 'god']])

    def test_hw19_2(self):
        list_of_words = ['act', 'pin', 'nip', 'cat', 'dog', 'god', 'tac', 'rop', 'por']
        self.assertEqual(hw19_1(list_of_words), [['act', 'cat', 'tac'], ['pin', 'nip'], ['dog', 'god'], ['rop', 'por']])

    def test_is_subset(self):
        set1 = {1, 2, 3}
        set2 = {1, 2, 3, 4, 5}
        self.assertEqual(is_subset(set1, set2), True)
        set1 = {1, 2, 3}
        set2 = {4, 5, 6, 3, 2, 1}
        self.assertEqual(is_subset(set1, set2), True)
        set1 = {1, 2, 3}
        set2 = {4, 5, 6}
        self.assertEqual(is_subset(set1, set2), False)


if __name__ == '__main__':
    unittest.main()
