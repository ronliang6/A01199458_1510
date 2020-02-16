import io
from unittest import TestCase
from unittest.mock import patch

import dnd


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_with_items(self, output):
        dnd.print_character({"Name": "Solar",
                             "Strength": 26,
                             "Intelligence": 25,
                             "Wisdom": 25,
                             "Dexterity": 14,
                             "Constitution": 26,
                             "Charisma": 30,
                             "Inventory": ["Angelic Weapons", "Divine Awareness", "Innate Spellcasting"],
                             "XP": 33000,
                             "Class": "paladin",
                             "Race": "human",
                             "HP": [35, 10]})
        expected = "Name: Solar\nStrength: 26\nIntelligence: 25\nWisdom: 25\nDexterity: 14\nConstitution: 26\n" \
                   "Charisma: 30\nInventory:\nAngelic Weapons\nDivine Awareness\nInnate Spellcasting\nXP: 33000\n" \
                   "Class: paladin\nRace: human\nHP: 10/35\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_no_items(self, output):
        dnd.print_character({"Name": "Solar",
                             "Strength": 26,
                             "Intelligence": 25,
                             "Wisdom": 25,
                             "Dexterity": 14,
                             "Constitution": 26,
                             "Charisma": 30,
                             "Inventory": [],
                             "XP": 33000,
                             "Class": "paladin",
                             "Race": "human",
                             "HP": [35, 10]})
        expected = "Name: Solar\nStrength: 26\nIntelligence: 25\nWisdom: 25\nDexterity: 14\nConstitution: 26\n" \
                   "Charisma: 30\nInventory:\nXP: 33000\nClass: paladin\nRace: human\nHP: 10/35\n"
        self.assertEqual(output.getvalue(), expected)
