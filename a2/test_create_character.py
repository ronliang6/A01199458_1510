import io
from unittest import TestCase
from unittest.mock import patch

import dnd


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_syllables_not_int(self, output):
        dnd.create_character("hello")
        expected = "You have failed to enter a positive integer.\n"
        self.assertEqual(expected, output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_syllables_negative_int(self, output):
        dnd.create_character("-12")
        expected = "You have failed to enter a positive integer.\n"
        self.assertEqual(expected, output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_syllables_zero(self, output):
        dnd.create_character("0")
        expected = "You have failed to enter a positive integer.\n"
        self.assertEqual(expected, output.getvalue())

    @patch('dnd.roll_hit_dice', side_effect=[6])
    @patch('dnd.select_race', side_effect=["elf"])
    @patch('dnd.select_class', side_effect=["bard"])
    @patch('dnd.roll_die', side_effect=[4, 5, 6, 7, 8, 9])
    @patch('dnd.generate_name', side_effect=["Yy"])
    def test_create_character_syllables_one(self, _, __, ___, ____, _____):
        actual = dnd.create_character("1")
        expected = {"Name": "Yy", "Strength": 4, "Intelligence": 5, "Wisdom": 6, "Dexterity": 7, "Constitution": 8,
                    "Charisma": 9, "Inventory": [], "XP": 0, "Class": "bard", "Race": "elf", "HP": [6, 6]}
        self.assertEqual(expected, actual)

    @patch('dnd.roll_hit_dice', side_effect=[6])
    @patch('dnd.select_race', side_effect=["elf"])
    @patch('dnd.select_class', side_effect=["bard"])
    @patch('dnd.roll_die', side_effect=[4, 5, 6, 7, 8, 9])
    @patch('dnd.generate_name', side_effect=["Yyhisubuse"])
    def test_create_character_syllables_one(self, _, __, ___, ____, _____):
        actual = dnd.create_character("5")
        expected = {"Name": "Yyhisubuse", "Strength": 4, "Intelligence": 5, "Wisdom": 6, "Dexterity": 7, "Constitution": 8,
                    "Charisma": 9, "Inventory": [], "XP": 0, "Class": "bard", "Race": "elf", "HP": [6, 6]}
        self.assertEqual(expected, actual)

    @patch('dnd.roll_hit_dice', side_effect=[6])
    @patch('dnd.select_race', side_effect=["elf"])
    @patch('dnd.select_class', side_effect=["bard"])
    @patch('dnd.roll_die', side_effect=[4, 5, 6, 7, 8, 9])
    @patch('dnd.generate_name', side_effect=["Yyhisubuseyyhisubuse"])
    def test_create_character_syllables_many(self, _, __, ___, ____, _____):
        actual = dnd.create_character("10")
        expected = {"Name": "Yyhisubuseyyhisubuse", "Strength": 4, "Intelligence": 5, "Wisdom": 6, "Dexterity": 7,
                    "Constitution": 8,
                    "Charisma": 9, "Inventory": [], "XP": 0, "Class": "bard", "Race": "elf", "HP": [6, 6]}
        self.assertEqual(expected, actual)