import random
import string


def create_name(length):
    """Generate a title case string of random letters of a given length and return none if given a non-whole-number."""

    if str.isdigit(str(length)):
        random_string = ""
        for x in range(int(length)):
            random_string += random.choice(string.ascii_letters)
        return random_string.title()
    else:
        return None


def roll_die():
    """ Calculate a sum, randomly selecting integers within a inputted range an inputted number of times.

    If either parameter is less than one, return 0. If not, then randomly select an integer within the range [1,
    number_of_sides] a number of times equal to number_of_rolls, and then return that result.
    """

    print("Welcome to my dice rolling program! You can enter the number of dice that you are rolling as well as how "
          "many sides you want the dice to have")
    number_of_rolls = input("Please enter the number of dice that you wish to roll")
    number_of_sides = input("Please enter the number of sides that you wish your dice to have")

    if int(number_of_rolls) > 0 and int(number_of_sides) > 0:

        sum_of_rolls = 0

        for x in range(int(number_of_rolls)):
            sum_of_rolls += random.randint(1, int(number_of_sides))

        return sum_of_rolls

    else:
        return 0


def main():
    """Call and print the roll_die and create_name functions."""

    print("You rolled: " + str(roll_die()) + ". Hope it was good. Unless you're my DM.")

    print("Your random string is: " + str(create_name(15)))
    print("Your random string is: " + str(create_name("a")))


if __name__ == "__main__":
    """Call the main method if this is the main program."""

    main()
