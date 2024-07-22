import unittest
from hw.hw_32 import Counter, Email


class TestHomeworkFunction(unittest.TestCase):

    def test_hw32_1(self):
        def test_addition(self):
            counter = Counter(5)
            counter += 3
            self.assertEqual(int(counter), 8)

        def test_subtraction(self):
            counter = Counter(5)
            counter -= 2
            self.assertEqual(int(counter), 3)

        def test_str_representation(self):
            counter = Counter(5)
            self.assertEqual(str(counter), '5')

        def test_int_conversion(self):
            counter = Counter(5)
            self.assertEqual(int(counter), 5)

    def test_hw32_2(self):
        def setUp(self):
            self.email1 = Email("john@example.com", "jane@example.com", "Meeting",
                                "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
            self.email2 = Email("jane@example.com", "john@example.com", "Re: Meeting",
                                "Sure, let's meet at 2 PM.", "2022-05-10")
            self.email3 = Email("alice@example.com", "bob@example.com", "Hello",
                                "Hi Bob, how are you?", "2022-05-09")

        def test_comparison(self):
            self.assertTrue(self.email2 > self.email3)
            self.assertFalse(self.email3 > self.email2)

        def test_str_representation(self):
            expected_str = "From: john@example.com\nTo: jane@example.com\nSubject: Meeting\nHi Jane, let's have a meeting tomorrow."
            self.assertEqual(str(self.email1), expected_str)

        def test_length(self):
            self.assertEqual(len(self.email2), 24)

        def test_hash(self):
            self.assertIsInstance(hash(self.email3), int)

        def test_bool(self):
            self.assertTrue(bool(self.email1))


if __name__ == '__main__':
    unittest.main()
