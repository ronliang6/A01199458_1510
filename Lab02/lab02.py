"""
Functions to randomly generate numbers and strings.
"""

import random
import string


def positive_integer_test(test):
    """
    Determine if a string is a positive integer.

    :param test: a string
    :return: if test is a positive integer, return True, otherwise return False.
    """

    if str.isdigit(str(test)):
        if int(test) > 0:
            return True
        else:
            return False
    else:
        return False


def create_name(length):
    """
    Create a title-cased string of random letters of a given length.

    :param length: a positive integer
    :return: a string
    """
    return random_name(length, "")


def random_name(length, random_string):
    """
    Create a title-cased string of random letters of a given length.

    :param length: a positive integer
    :param random_string: a string
    :return: a string
    """
    if positive_integer_test(length):

        if len(random_string) < length:
            random_string += random.choice(string.ascii_letters)
            return random_name(length, random_string)
        else:
            return random_string.title()
    else:
        return None


def roll_die(number_of_rolls, number_of_sides):
    """
    Calculate a sum, randomly selecting integers within a inputted range an inputted number of times.

    Rolls a given number of dice with a given number of sides. If either given number is not a positive integer,
    return 0.

    :param number_of_rolls: an integer representing the number of dice you want to roll
    :param number_of_sides: an integer representing the number of sides per dice rolled
    :return: return 0 if inputs are not positive integers, else return the sum.
    """

    return die_roller(number_of_rolls, number_of_sides, 0, 0)


def die_roller(number_of_rolls, number_of_sides, sum_of_rolls, rolled_dice):
    """
    Roll dice with a given number of sides randomly, a given number of times and return that number.

    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :param sum_of_rolls: an integer that sums the dice rolls
    :param rolled_dice: an integer that tracks how many dice have been rolled
    :return: an integer that is sum_of_rolls
    """

    if positive_integer_test(number_of_rolls) and positive_integer_test(number_of_sides):
        if rolled_dice < int(number_of_rolls):
            sum_of_rolls += random.randint(1, int(number_of_sides))
            rolled_dice += 1
            return die_roller(number_of_rolls, number_of_sides, sum_of_rolls, rolled_dice)
        else:
            return sum_of_rolls
    else:
        return 0


def main():
    """Call and print the roll_die and create_name functions."""

    # roll_dice function test
    print("Welcome to my dice rolling program! You can enter the number of dice that you are rolling as well as how "
          "many sides you want the dice to have")
    number_of_rolls = input("Please enter the number of dice that you wish to roll")
    number_of_sides = input("Please enter the number of sides that you wish your dice to have")
    print("You rolled: " + str(roll_die(number_of_rolls, number_of_sides)) + ". Hope it was good. Unless you're my DM.")

    # create_name function tests
    print("Your random string is: " + str(create_name(10)))
    print("Your random string is: " + str(random_name("a")))


if __name__ == "__main__":
    main()
