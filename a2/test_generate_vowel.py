from unittest import TestCase

from a2.dnd import generate_vowel


class Test(TestCase):
    def test_generate_vowel_many_times(self):
        does_pass = True
        for _ in range(1000):
            if generate_vowel() not in "aeiouy":
                does_pass = False
        self.assertTrue(does_pass)
