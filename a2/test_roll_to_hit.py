from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('dnd.roll_hit_dice', side_effect=[3])
    @patch('dnd.roll_die', side_effect=[16])
    def test_roll_to_hit_hit(self, _, __):
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
        dnd.roll_to_hit(attacker, defender)
        actual = defender["HP"][1]
        expected = 2
        self.assertEqual(actual, expected)

    @patch('dnd.roll_die', side_effect=[12])
    def test_roll_to_hit_miss(self, _):
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
        dnd.roll_to_hit(attacker, defender)
        actual = defender["HP"][1]
        expected = 5
        self.assertEqual(actual, expected)

    @patch('dnd.roll_die', side_effect=[14])
    def test_roll_to_hit_roll_equals_dexterity(self, _):
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
        dnd.roll_to_hit(attacker, defender)
        actual = defender["HP"][1]
        expected = 5
        self.assertEqual(actual, expected)