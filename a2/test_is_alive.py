from unittest import TestCase

import dnd


class Test(TestCase):
    def test_is_alive_HP_max(self):
        actual = dnd.is_alive({"Name": "Solar",
                               "Strength": 26,
                               "Intelligence": 25,
                               "Wisdom": 25,
                               "Dexterity": 14,
                               "Constitution": 26,
                               "Charisma": 30,
                               "Inventory": ["Angelic Weapons", "Divine Awareness", "Innate Spellcasting"],
                               "XP": 33000,
                               "Class": "Paladin",
                               "Race": "human",
                               "HP": [35, 35]})
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_HP_zero(self):
        actual = dnd.is_alive({"Name": "Solar",
                               "Strength": 26,
                               "Intelligence": 25,
                               "Wisdom": 25,
                               "Dexterity": 14,
                               "Constitution": 26,
                               "Charisma": 30,
                               "Inventory": ["Angelic Weapons", "Divine Awareness", "Innate Spellcasting"],
                               "XP": 33000,
                               "Class": "Paladin",
                               "Race": "human",
                               "HP": [35, 0]})
        expected = False
        self.assertEqual(actual, expected)

    def test_is_alive_HP_negative(self):
        actual = dnd.is_alive({"Name": "Solar",
                               "Strength": 26,
                               "Intelligence": 25,
                               "Wisdom": 25,
                               "Dexterity": 14,
                               "Constitution": 26,
                               "Charisma": 30,
                               "Inventory": ["Angelic Weapons", "Divine Awareness", "Innate Spellcasting"],
                               "XP": 33000,
                               "Class": "Paladin",
                               "Race": "human",
                               "HP": [35, -23]})
        expected = False
        self.assertEqual(actual, expected)