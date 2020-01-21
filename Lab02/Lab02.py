import random


def roll_die(number_of_rolls, number_of_sides):
    """ Calculate a sum, randomly selecting integers within a range a given number of times, if the given parameters
    are both positive integers.

    If either parameter is less than one, return 0. If not, then randomly select an integer within the range [1,
    number_of_sides] a number of times equal to number_of_rolls, and then return that result.
    """

    if int(number_of_rolls) > 0 and int(number_of_sides) > 0:

        sum_of_rolls = 0

        for x in range(int(number_of_rolls)):
            sum_of_rolls += random.randint(1, int(number_of_sides))

        return sum_of_rolls

    else:
        return 0


def main():
    print("Welcome to my dice rolling program! You can enter the number of dice that you are rolling as well as how "
          "many sides you want the dice to have.")
    number_of_rolls = input("Please enter the number of dice that you wish to roll")
    number_of_sides = input("Please enter the number of sides that you wish your dice to have")
    print("You rolled: " + str(roll_die(number_of_rolls, number_of_sides)) + ". Hope it was good. "
                                                                             "Unless you're the DM.")


if __name__ == "__main__":
    main()
