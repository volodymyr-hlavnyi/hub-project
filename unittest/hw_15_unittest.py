import unittest
from hw.hw_15 import hw15_1, hw15_2


class TestHomeworkFunction(unittest.TestCase):

    def test_hw15_1_1(self):
        students = [('Alice', 20, 90), ('Bob', 19, 80), ('Charlie', 21, 95), ('David', 18, 85)]
        threshold = 90
        self.assertEqual(hw15_1(students, threshold), ['Charlie'])

    def test_hw15_1_2(self):
        students = [('Alice', 20, 90), ('Bob', 19, 80), ('Charlie', 21, 95), ('David', 18, 85)]
        threshold = 85
        self.assertEqual(hw15_1(students, threshold), ['Alice', 'Charlie'])

    def test_hw15_2_1(self):
        sentence = 'Программирование это интересно и полезно'
        self.assertEqual(hw15_2(sentence), (16, 3, 9, 1, 7))

    def test_hw15_2_2(self):
        sentence = 'Programming is interesting and useful'
        self.assertEqual(hw15_2(sentence), (11, 2, 11, 3, 6))


if __name__ == '__main__':
    unittest.main()
