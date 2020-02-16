from unittest import TestCase
from unittest.mock import patch

import dnd


class Test(TestCase):
    @patch('dnd.roll_initiative', side_effect=["Solar"])
    @patch('dnd.roll_die', side_effect=[15])
    @patch('dnd.roll_hit_dice', side_effect=[6])
    def test_combat_round_character1_hit_and_kill(self, _, __, ___):
        char_one = {"Name": "Solar",
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
        char_two = {"Name": "Solar2",
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
        dnd.combat_round(char_one, char_two)
        actual = [char_one["HP"][1], char_two["HP"][1]]
        expected = [5, -1]
        self.assertEqual(actual, expected)

    @patch('dnd.roll_initiative', side_effect=["Solar"])
    @patch('dnd.roll_die', side_effect=[15, 16])
    @patch('dnd.roll_hit_dice', side_effect=[4, 3])
    def test_combat_round_character1_hit_character2_hit(self, _, __, ___):
        char_one = {"Name": "Solar",
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
        char_two = {"Name": "Solar2",
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
        dnd.combat_round(char_one, char_two)
        actual = [char_one["HP"][1], char_two["HP"][1]]
        expected = [2, 1]
        self.assertEqual(actual, expected)

    @patch('dnd.roll_initiative', side_effect=["Solar"])
    @patch('dnd.roll_die', side_effect=[12, 16])
    @patch('dnd.roll_hit_dice', side_effect=[3])
    def test_combat_round_character1_miss_character2_hit(self, _, __, ___):
        char_one = {"Name": "Solar",
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
        char_two = {"Name": "Solar2",
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
        dnd.combat_round(char_one, char_two)
        actual = [char_one["HP"][1], char_two["HP"][1]]
        expected = [2, 5]
        self.assertEqual(actual, expected)

    @patch('dnd.roll_initiative', side_effect=["Solar"])
    @patch('dnd.roll_die', side_effect=[12, 11])
    def test_combat_round_both_miss(self, _, __):
        char_one = {"Name": "Solar",
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
        char_two = {"Name": "Solar2",
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
        dnd.combat_round(char_one, char_two)
        actual = [char_one["HP"][1], char_two["HP"][1]]
        expected = [5, 5]
        self.assertEqual(actual, expected)

    @patch('dnd.roll_initiative', side_effect=["Solar"])
    @patch('dnd.roll_die', side_effect=[19, 11])
    @patch('dnd.roll_hit_dice', side_effect=[3])
    def test_combat_round_character1_hit_character2_miss(self, _, __, ___):
        char_one = {"Name": "Solar",
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
        char_two = {"Name": "Solar2",
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
        dnd.combat_round(char_one, char_two)
        actual = [char_one["HP"][1], char_two["HP"][1]]
        expected = [5, 2]
        self.assertEqual(actual, expected)

    @patch('dnd.roll_initiative', side_effect=["Solar"])
    @patch('dnd.roll_die', side_effect=[19, 20])
    @patch('dnd.roll_hit_dice', side_effect=[3, 6])
    def test_combat_round_character1_hit_character2_hit_and_kill(self, _, __, ___):
        char_one = {"Name": "Solar",
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
        char_two = {"Name": "Solar2",
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
        dnd.combat_round(char_one, char_two)
        actual = [char_one["HP"][1], char_two["HP"][1]]
        expected = [-1, 2]
        self.assertEqual(actual, expected)