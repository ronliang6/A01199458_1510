from unittest import TestCase
from unittest.mock import patch

import dnd


class Test(TestCase):
    @patch('builtins.input', side_effect=["1", "-1"])
    def test_choose_inventory_buy_first_item(self, _):
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
        dnd.choose_inventory(char_one)
        actual = char_one["Inventory"]
        expected = ["Ring of Three Wishes"]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["5", "-1"])
    def test_choose_inventory_buy_fifth_item(self, _):
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
        dnd.choose_inventory(char_one)
        actual = char_one["Inventory"]
        expected = ["Potion Seller's Store"]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["10", "-1"])
    def test_choose_inventory_buy_last_item(self, _):
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
        dnd.choose_inventory(char_one)
        actual = char_one["Inventory"]
        expected = ["A Bonus Mark"]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["0", "76", "12", "-1"])
    def test_choose_inventory_out_of_range_integers(self, _):
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
        dnd.choose_inventory(char_one)
        actual = char_one["Inventory"]
        expected = []
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["a", " ", "dfg34ferf ", "-1"])
    def test_choose_inventory_multiple_NaN(self, _):
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
        dnd.choose_inventory(char_one)
        actual = char_one["Inventory"]
        expected = []
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["1", "4", "5", "7", "-1"])
    def test_choose_inventory_multiple_different_purchases(self, _):
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
        dnd.choose_inventory(char_one)
        actual = char_one["Inventory"]
        expected = ["Ring of Three Wishes", "Your Local Politician", "Potion Seller's Store",
                    "A Spherical Muffin Where There Is Only Top-Muffin"]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["1", "1", "1", "1", "-1"])
    def test_choose_inventory_multiple_same_purchases(self, _):
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
        dnd.choose_inventory(char_one)
        actual = char_one["Inventory"]
        expected = ["Ring of Three Wishes", "Ring of Three Wishes", "Ring of Three Wishes", "Ring of Three Wishes"]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["1", "asdasf23 ", "5", "122", "1", "g2323", "w", "gelooeg", "4", "2", "-1"])
    def test_choose_inventory_all_input_partitions(self, _):
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
        dnd.choose_inventory(char_one)
        actual = char_one["Inventory"]
        expected = ["Ring of Three Wishes", "Potion Seller's Store", "Ring of Three Wishes", "Your Local Politician",
                    "Chris Thompson's Shorts (his favorite beige pair)"]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["1", "asdasf23 ", "5", "122", "1", "g2323", "w", "gelooeg", "4", "2", "-1"])
    def test_choose_inventory_character_has_items(self, _):
        char_one = {"Name": "Solar",
                    "Strength": 26,
                    "Intelligence": 25,
                    "Wisdom": 25,
                    "Dexterity": 14,
                    "Constitution": 26,
                    "Charisma": 30,
                    "Inventory": ["Legendary spanakopita"],
                    "XP": 33000,
                    "Class": "paladin",
                    "Race": "human",
                    "HP": [35, 5]}
        dnd.choose_inventory(char_one)
        actual = char_one["Inventory"]
        expected = ["Legendary spanakopita", "Ring of Three Wishes", "Potion Seller's Store", "Ring of Three Wishes",
                    "Your Local Politician", "Chris Thompson's Shorts (his favorite beige pair)"]
        self.assertEqual(actual, expected)