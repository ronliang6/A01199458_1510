from unittest import TestCase
import regular_expressions


class Test(TestCase):
    def test_is_email_lower_case_username(self):
        actual = regular_expressions.is_email("a@gmail.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_upper_case_username(self):
        actual = regular_expressions.is_email("A@gmail.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_number_username(self):
        actual = regular_expressions.is_email("0@gmail.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_alphanumeric_username(self):
        actual = regular_expressions.is_email("A010gsz@gmail.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_symbol_username(self):
        actual = regular_expressions.is_email("!~@@gmail.com")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_empty_username(self):
        actual = regular_expressions.is_email("@gmail.com")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_missing_period(self):
        actual = regular_expressions.is_email("A010gsz@gmailcom")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_period_in_top_level_domain(self):
        actual = regular_expressions.is_email("A010gsz@gmail..com")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_two_top_level_domains(self):
        actual = regular_expressions.is_email("A010gsz@gmail.com.com")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_empty_string(self):
        actual = regular_expressions.is_email("")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_empty_domain(self):
        actual = regular_expressions.is_email("A010gsz@.com")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_empty_top_level_domain(self):
        actual = regular_expressions.is_email("A010gsz@gmail")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_top_level_domain_too_long(self):
        actual = regular_expressions.is_email("A010gsz@gmail.comca")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_top_level_domain_too_short(self):
        actual = regular_expressions.is_email("A010gsz@gmail.c")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_space_in_username(self):
        actual = regular_expressions.is_email("A01 0gsz@gmail.com")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_string_after_top_level_domain(self):
        actual = regular_expressions.is_email("A010gsz@gmail.com hello")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_string_before_username(self):
        actual = regular_expressions.is_email("hello A010gsz@gmail.com")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_whitespace_before_username(self):
        actual = regular_expressions.is_email(" A010gsz@gmail.com")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_whitespace_ended_top_level_domain(self):
        actual = regular_expressions.is_email("A010gsz@gmail.com ")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_whitespace_in_top_level_domain(self):
        actual = regular_expressions.is_email("A010gsz@gmail.c om")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_swapped_domains(self):
        actual = regular_expressions.is_email("A010gsz.com@gmail")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_underscore_in_username(self):
        actual = regular_expressions.is_email("A010_gsz@gmail.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_symbols_as_top_level_domain(self):
        actual = regular_expressions.is_email("A010gsz@gmail.@.@@")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_symbol_in_domain(self):
        actual = regular_expressions.is_email("A010gsz@g-mail.com")
        expected = False
        self.assertEqual(actual, expected)
