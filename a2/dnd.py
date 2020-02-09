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
    Return a random vowel (including "y").

    :precondition: provide the function with no arguments.
    :postcondition: return an object as defined by the return statement below.
    :return: a string of length one that is a vowel (including y).
    """
    return random.choice("aeiouy")


def generate_consonant():
    """
    Return a random consonant (including y).

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
                     "XP": 0}
        return character

e
def select_class():
    """
    Ask the user to select a class and then return that class as a string.

    :precondition: TODO
    :postcondition: return an object as defined by the return statement below.
    :return: a string representing the class of the character.
    """
    character_class = input("Please pick a class from the following list: "
                            "Fighter, Rogue, Monk, Ranger, Wizard, Warlock, Sorcerer, Cleric, Druid, Bard, Barbarian, "
                            "Paladin.")
    return character_class


def main():
    doctest.testmod()
    print(roll_die(1, 10))


if __name__ == "__main__":
    main()
