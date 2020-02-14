from unittest import TestCase

from a2.dnd import generate_consonant


class Test(TestCase):
    def test_generate_consonant(self):
        does_pass = True
        for _ in range(1000):
            if generate_consonant() not in "bcdfghjklmnpqrstvwxyz":
                does_pass = False
        self.assertTrue(does_pass)
