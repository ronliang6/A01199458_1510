from unittest import TestCase
import regular_expressions


class Test(TestCase):
    def test_is_nakamoto_typical_valid(self):
        actual = regular_expressions.is_nakamoto("Naruto Nakamoto")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_nakamoto_one_letter_first_name(self):
        actual = regular_expressions.is_nakamoto("N Nakamoto")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_nakamoto_no_space_between_names(self):
        actual = regular_expressions.is_nakamoto("NarutoNakamoto")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_no_first_name(self):
        actual = regular_expressions.is_nakamoto(" Nakamoto")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_lower_case_first_name(self):
        actual = regular_expressions.is_nakamoto("naruto Nakamoto")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_first_name_middle_char_capitalized(self):
        actual = regular_expressions.is_nakamoto("naRuto Nakamoto")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_only_last_name(self):
        actual = regular_expressions.is_nakamoto("Nakamoto")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_lowercase_last_name(self):
        actual = regular_expressions.is_nakamoto("naRuto nakamoto")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_different_spelling_last_name(self):
        actual = regular_expressions.is_nakamoto("Naruto Nekomoto")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_leading_space(self):
        actual = regular_expressions.is_nakamoto(" Naruto Nakamoto")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_trailing_space(self):
        actual = regular_expressions.is_nakamoto("Naruto Nakamoto ")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_long_first_name(self):
        actual = regular_expressions.is_nakamoto("Narutonarutonaruto Nakamoto")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_nakamoto_same_names(self):
        actual = regular_expressions.is_nakamoto("Nakamoto Nakamoto")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_nakamoto_with_middle_name(self):
        actual = regular_expressions.is_nakamoto("Naruto Uzumaki Nakamoto")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_symbol_in_first_name(self):
        actual = regular_expressions.is_nakamoto("Naka-moto Nakamoto")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_nakamoto_number_in_first_name(self):
        actual = regular_expressions.is_nakamoto("Naru2 Nakamoto")
        expected = False
        self.assertEqual(actual, expected)
