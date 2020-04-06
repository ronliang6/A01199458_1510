from unittest import TestCase
import regular_expressions


class Test(TestCase):
    def test_is_poker_empty_string(self):
        actual = regular_expressions.is_poker("")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_poker_one_char(self):
        actual = regular_expressions.is_poker("a")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_poker_too_short_string(self):
        actual = regular_expressions.is_poker("aaaa")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_poker_too_long_string(self):
        actual = regular_expressions.is_poker("aj2376")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_poker_very_long_string(self):
        actual = regular_expressions.is_poker("a2a898q3kjq")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_poker_invalid_letters(self):
        actual = regular_expressions.is_poker("hello")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_poker_invalid_number(self):
        actual = regular_expressions.is_poker("23461")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_poker_five_identical_cards(self):
        actual = regular_expressions.is_poker("88888")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_poker_only_valid_numbers(self):
        actual = regular_expressions.is_poker("59342")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_poker_high_card_mix(self):
        actual = regular_expressions.is_poker("jkqt5")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_poker_one_pair(self):
        actual = regular_expressions.is_poker("33taq")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_poker_two_pair(self):
        actual = regular_expressions.is_poker("ttkka")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_poker_straight(self):
        actual = regular_expressions.is_poker("789tj")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_poker_full_hoyse(self):
        actual = regular_expressions.is_poker("88822")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_poker_four_of_a_kind(self):
        actual = regular_expressions.is_poker("3333a")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_poker_straight_flush_ignoring_suits(self):
        actual = regular_expressions.is_poker("tjqka")
        expected = True
        self.assertEqual(actual, expected)
