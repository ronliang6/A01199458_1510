from unittest import TestCase
import file_io


class Test(TestCase):
    def test_string_cleaner_empty_string(self):
        actual = file_io.string_cleaner("")
        expected = ""
        self.assertEqual(actual, expected)

    def test_string_cleaner_one_symbol(self):
        actual = file_io.string_cleaner(",")
        expected = " "
        self.assertEqual(actual, expected)

    def test_string_cleaner_all_symbols(self):
        actual = file_io.string_cleaner(".,()/")
        expected = "     "
        self.assertEqual(actual, expected)

    def test_string_cleaner_numbers(self):
        actual = file_io.string_cleaner("123123")
        expected = "123123"
        self.assertEqual(actual, expected)

    def test_string_cleaner_mixed_characters(self):
        actual = file_io.string_cleaner('2r5 3z,. 1(')
        expected = '2r5 3z   1 '
        self.assertEqual(actual, expected)

    def test_string_cleaner_no_symbols(self):
        actual = file_io.string_cleaner("hello how are you")
        expected = "hello how are you"
        self.assertEqual(actual, expected)
