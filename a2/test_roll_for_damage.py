from unittest import TestCase
from unittest.mock import patch

import dnd


class Test(TestCase):
    @patch('dnd.roll_hit_dice', side_effect=[6])
    def test_roll_for_damage_lethal(self, _):
        attacker = {"Name": "Solar",
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
                    "HP": [35, 5]}
        defender = {"Name": "Solar2",
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
                    "HP": [35, 5]}
        dnd.roll_for_damage(attacker, defender)
        actual = defender["HP"][1]
        expected = -1
        self.assertEqual(actual, expected)

    @patch('dnd.roll_hit_dice', side_effect=[4])
    def test_roll_for_damage_not_lethal(self, _):
        attacker = {"Name": "Solar",
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
                    "HP": [35, 5]}
        defender = {"Name": "Solar2",
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
                    "HP": [35, 5]}
        dnd.roll_for_damage(attacker, defender)
        actual = defender["HP"][1]
        expected = 1
        self.assertEqual(actual, expected)
