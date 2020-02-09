import doctest
import random


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


def main():
    doctest.testmod()
    print(generate_name(19))


if __name__ == "__main__":
    main()
