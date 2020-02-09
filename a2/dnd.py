import doctest
import random


def roll_die(number_of_rolls, number_of_sides):
    """
    Simulate rolling dice with a chosen number of sides a chosen number of times.

    :param number_of_rolls: a positive integer representing the number of times the dice should be rolled.
    :param number_of_sides: a positive integer representing the number of sides the dice have.
    :precondition: provide valid arguments to the function as defined by the PARAM statements above.
    :postcondition: return an object as defined by the return statement below.
    :return: a positive integer representing the sum of the dice rolls.
    """
    dice_sum = 0
    for i in range(number_of_rolls):
        dice_sum += random.randint(1, number_of_sides)
    return dice_sum


def generate_name(syllables):
    """
    Generate a simple random name of alternating consonants and vowels.

    :param syllables: a positive integer.
    :precondition: provide the function with a valid argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a random string representing a name.
    """
    name = ""
    for i in range(syllables):
        name += generate_syllable()
    return name


def generate_syllable():
    """
    Generate a random syllable composed of a random consonant followed by a random vowel.

    :precondition: provide the function with no arguments.
    :postcondition: return an object as defined by the return statement below.
    :return: a string of length two composed of a consonant followed by a vowel.
    """
    return generate_consonant() + generate_vowel()


def generate_vowel():
    """
    Generate and return a random vowel (including "y").

    :precondition: provide the function with no arguments.
    :postcondition: return an object as defined by the return statement below.
    :return: a string of length one that is a vowel (including y).
    """
    return random.choice("aeiouy")


def generate_consonant():
    """
    Generate and return a random consonant (including y).

    :precondition: provide the function with no arguments.
    :postcondition: return an object as defined by the return statement below.
    :return: a string of length one that is a consonant (including y).
    """
    return random.choice("bcdfghjklmnpqrstvwxyz")


def create_character(syllables):
    if type(syllables) != int or syllables <= 0:
        print("You have failed to enter a positive integer.")
    else:
        name = generate_name(syllables)
        character = {"Name": name,
                     "Strength": roll_die(3, 6),
                     "Intelligence": roll_die(3, 6),
                     "Wisdom": roll_die(3, 6),
                     "Dexterity": roll_die(3, 6),
                     "Constitution": roll_die(3, 6),
                     "Charisma": roll_die(3, 6),
                     "Inventory": [],
                     "XP": 0,
                     "Class": select_class(),
                     "Race": select_race()}
        character_health = hp_initializer(character["Class"])
        character["HP"] = [character_health, character_health]
        return character


def hp_initializer(character_class):
    """
    Generate the starting health for a character based on it's class.

    :param character_class: a string that is a Dungeons and Dragons class in lower case letters.
    :precondition: provide the function with a valid argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: an integer representing the starting health of that character.
    """
    if character_class == "barbarian":
        return roll_die(1, 12)
    elif character_class in ["fighter", "paladin", "ranger"]:
        return roll_die(1, 10)
    elif character_class in ["bard", "cleric", "druid", "monk", "rogue", "warlock"]:
        return roll_die(1, 8)
    else:
        return roll_die(1, 6)


def select_class():
    """
    Ask the user to select a class and then return that class as a string.

    :precondition: TODO
    :postcondition: return an object as defined by the return statement below.
    :return: a string representing the class of the character.
    """
    character_class = input("Please pick a class from the following list: "
                            "Fighter, Rogue, Monk, Ranger, Wizard, Warlock, Sorcerer, Cleric, Druid, Bard, Barbarian, "
                            "and Paladin.")
    return character_class.lower()


def select_race():
    """
    Ask the user to select a race and then return that race as a string.

    :precondition: TODO
    :postcondition: return an object as defined by the return statement below.
    :return: a string representing the race of the character.
    """
    character_race = input("Please pick a class from the following list: "
                           "Tiefling, Dragonborn, Human, Half-Elf, Elf, Dwarf, Gnome, Halfling, and Half-Orc.")
    return character_race.lower()


def print_character(character):
    """
    Print the provided argument.

    :param character: a printable object.
    :precondition: provide the function with a valid argument as defined by the PARAM statement above.
    :postcondition: print the provided argument.
    """
    print(character)


def choose_inventory(character):
    shop_message = """    Welcome to the Potion Seller's Store!
    You cannot handle my strongest potions..
    
    So here are some non-potion wares!
    
    1. Short Sword + 10
    2. Armor of Invulnerability
    3. Ring of Three Wishes
    4. Beretta M9A1 with 60 Rounds of 9mm Ammunition
    5. Potion Seller's Store
    
    What would you like to buy?
    (Please enter a list number to buy that item or -1 to leave my store)"""

    items = ["Short Sword + 10", "Armor of Invulnerability", "Ring of Three Wishes",
             "Beretta M9A1 with 60 Rounds of 9mm Ammunition", "Potion Seller's Store"]
    shopping_basket = []

    purchase = input(shop_message)
    while purchase != "-1":
        if purchase.isdigit() and int(purchase) in [1, 2, 3, 4, 5]:
            shopping_basket.append(items[int(purchase)-1])
            purchase = input(shop_message)
        else:
            print("Please enter an integer in the range [1,5] or -1.")
            purchase = input(shop_message)
    character["Inventory"].extend(shopping_basket)


def main():
    doctest.testmod()
    x = {"Inventory": []}
    choose_inventory(x)
    print(x)


if __name__ == "__main__":
    main()
