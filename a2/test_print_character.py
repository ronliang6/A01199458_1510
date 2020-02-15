import io
from unittest import TestCase
from unittest.mock import patch

import dnd


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character(self, output):
        actual = dnd.print_character({"Name": "Solar",
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
        expected = "Name: Solar\nStrength: 26\nIntelligence:\n25 Wisdom: 25\nDexterity: 14\nConstitution: 26\n" \
                   "Charisma: 30\nInventory:\nAngelic Weapons\nDivine Awareness\nInnate Spellcasting\nXP: 33000\n" \
                   "Class: Paladin\nRace: human\nHP: [35, 35]"
        self.assertEqual(output.getvalue(), expected)
