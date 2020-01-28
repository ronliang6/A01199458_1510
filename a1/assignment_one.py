"""

"""


import random
import doctest


def convert_to_roman_numeral(positive_int):
    """
    Translate a positive integer from decimal to roman numeral.

    Components of computational thinking:
    Translating a decimal number to a roman numeral is composed of translating each digit of a decimal number then
    appending those translations together. I demonstrated pattern matching here and then decomposition by creating a
    helper function that handled translating a single digit. Originally in the helper function digit_converter,
    I had five separate lists and manually selected the correct list for the translation. I realized that I could use
    the position parameter given to that function to select for the correct list in a list of lists and demonstrated
    automation.

    :param positive_int: a positive integer representing the decimal number.
    :precondition: the user must enter an integer in the range [1, 10000].
    :postcondition: the function will return a roman numeral number with the same numerical value as the given
    argument.
    :return:a string representing the roman numeral that has equal numerical value to the parameter positive_int.

    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    >>> convert_to_roman_numeral(3094)
    'MMMXCIV'
    """
    int_length = len(str(positive_int))
    roman_numeral = ""
    for i in range(int_length):
        roman_numeral = digit_converter(positive_int, i) + roman_numeral
    return roman_numeral


def digit_converter(positive_int, position):
    """
    Convert a digit from decimal to the roman numeral equivalent.

    :param positive_int: a positive integer in the range [1, 10000].
    :param position: an integer representing the position of the digit in the positive_int to be converted. Must be no
    greater than one less than the length of the positive_int.
    :precondition: the user must enter valid arguments according to the PARAM statements above.
    :postcondition: the function will correctly translate a digit to the roman numeral equivalent.
    :return: a string representing the roman numeral that has equal numerical value to the digit determined by both
    arguments.

    >>> digit_converter(1234, 0)
    'IV'
    >>> digit_converter(6789, 3)
    'MMMMMM'
    """
    roman_numeral_list = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                          ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                          ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                          ["", "M", "MM", "MMM", "MMMM", "MMMMM", "MMMMMM", "MMMMMMM", "MMMMMMMM", "MMMMMMMMM"],
                          ["", "MMMMMMMMMM"]]

    return roman_numeral_list[position][int(str(positive_int)[-(position + 1)])]


def colour_mixer():
    """
    Create the resulting secondary colour from two primary colours given as inputs.

    Components of computational thinking:
    I demonstrated decomposition by separating the actual colour mixing into a different function and handled all
    the input receiving and error statements in the primary function. The precondition for the helper function
    dictates that the function must receive two different primary colours. I believe I demonstrated a small
    improvement in my algorithm by not accounting for cases where the colours are the same, resulting in a more
    efficient function with less lines of code.

    :precondition: the user provides two inputs.
    :postcondition: print the correct secondary colour that results from mixing two primary colours or a useful error
    message.
    """
    first_colour = input("please enter a primary colour (red, yellow, or blue)")
    second_colour = input("please enter a different primary colour")
    if (first_colour == "red" or first_colour == "blue" or first_colour == "yellow") and \
            (second_colour == "red" or second_colour == "blue" or second_colour == "yellow"):
        if first_colour == second_colour:
            print("You have entered the same colour twice. "
                  "Please enter two different primary colours (red, yellow, or blue).")
        print(colour_combiner(first_colour, second_colour))
    else:
        print("You have entered at least one invalid colour. "
              "Please enter a primary colour (red, yellow, or blue) twice.")


def colour_combiner(first_colour, second_colour):
    """
    Create the resulting secondary colour from two different primary colours.

    :param first_colour: a string that is "yellow", "red", or "blue".
    :param second_colour: a string that is "yellow", "red", or "blue", but not the same string as first_colour.
    :precondition: the user must enter valid arguments according to the PARAM statements above.
    :postcondition: the function will return an object according to the return statement below.
    :return: a string that represents the secondary colour created by mixing the two primary colours provided as
    arguments.

    >>> colour_combiner("yellow", "red")
    'orange'
    >>> colour_combiner("blue", "yellow")
    'green'
    >>> colour_combiner("red", "blue")
    'purple'
    """
    if (first_colour == "yellow" or first_colour == "red") and (second_colour == "yellow" or second_colour == "red"):
        return "orange"
    elif (first_colour == "yellow" or first_colour == "blue") and (second_colour == "yellow" or second_colour ==
                                                                   "blue"):
        return "green"
    else:
        return "purple"


def time_calculator(seconds):
    """
    Convert time in seconds to time in days, hours, minutes, and seconds.

    Components of computational thinking:
    I demonstrated a good understanding of algorithms and automation by building this function that closely resembles
    how one might solve this problem in real life. I designed a recursive function to repeatedly reduce seconds by a
    fixed amount and increase the relevant time unit by one until there are not enough seconds to continue,
    at which point the function begins with the next time unit.

    :param seconds: a positive integer representing seconds.
    :precondition: the user must enter a valid argument according to the PARAM statement above.
    :postcondition: print the time in days, hours, minutes, and seconds.

    >>> time_calculator(0)
    0 0 0 0
    >>> time_calculator(90006)
    1 1 0 6
    """
    print(time_converter(seconds, 0, 0, 0))


def time_converter(seconds, days, hours, minutes):
    """
    Simplify time in days, hours, minutes, and seconds.

    Only the seconds is simplified into days, hours, and minutes. In some cases it is possible to have more minutes and
    hours than 59, however that situation will only occur in scenarios where the function is called with hours or
    minutes > 0.
    :param seconds: a non-negative integer representing seconds.
    :param days: a non-negative integer representing days.
    :param hours: a non-negative integer representing hours.
    :param minutes: a non-negative integer representing minutes.
    :precondition: the user must enter valid arguments according to the PARAM statements above
    :postcondition: the function will return an object according to the return statement below, where the seconds
    given will be simplified into the largest units of time possible.
    :return: a string representing time in days, hours, minutes, and seconds as integers separated by a space (" ").

    >>> time_converter(93784, 0, 0, 0)
    '1 2 3 4'
    >>> time_converter(90061, 23, 59, 59)
    '24 60 60 1'
    >>> time_converter(0, 0, 0, 0)
    '0 0 0 0'
    """
    if seconds >= 86400:
        return time_converter(seconds - 86400, days + 1, hours, minutes)
    elif seconds >= 3600:
        return time_converter(seconds - 3600, days, hours + 1, minutes)
    elif seconds >= 60:
        return time_converter(seconds - 60, days, hours, minutes + 1)
    else:
        return str(days) + " " + str(hours) + " " + str(minutes) + " " + str(seconds)


def compound_interest(principal, annual_interest, compound_frequency, time_years):
    """
    Calculate and return the new balance of an account when earning compound interest.

    :param principal: a float representing the original balance of the account.
    :param annual_interest: a float representing the fractional interest earned annually without compounding.
    :param compound_frequency: an integer representing the number of times interest is compounded a year.
    :param time_years: an integer representing the number of years the interest will accrue.
    :precondition: the user must enter valid arguments according to the PARAM statements above
    :postcondition: return the new balance of the account.
    :return: a float representing the new balance of an account that has accrued compound interest.

    >>> compound_interest(100.00, 0.1, 1, 2)
    121.00000000000001
    >>> compound_interest(2.00, 1.0, 2, 2)
    10.125
    """
    new_balance = principal * pow((1 + annual_interest/compound_frequency), (compound_frequency * time_years))
    return new_balance


def rock_paper_scissors():
    """
    Simulate one game of rock, paper, scissors.

    Components of computational thinking:
    I demonstrated decomposition by creating a helper function that determines whether or not a game is won or not
    given choices. I demonstrated generalization/abstraction by designing parts of my code to be easily scaled to
    include more choices. If I wanted to play rock, paper, scissors, lizard, spock, all I need to do is add those
    choices to game_choices and make some other relatively simple changes.

    :precondition: provide an input.
    :postcondition: a string that is an error message if they have entered an invalid input or one that informs the
    user whether they have won.
    """
    game_choices = ["rock", "paper", "scissors"]
    raw_input = input('Please enter "rock", "paper", or "scissors" to play this game.')
    player_choice = raw_input.strip().lower()
    if player_choice != "rock" and player_choice != "paper" and player_choice != "scissor":
        print('You have entered an invalid choice. The acceptable choices are "rock", "paper", or "scissors".')
    else:
        computer_choice = random.choice(game_choices)
        outcome = rock_paper_scissors_round(player_choice, computer_choice)
        print("The computer picked " + computer_choice + ". " + outcome)


def rock_paper_scissors_round(player_choice, computer_choice):
    """
    Decide whether or not a player won a game of rock paper scissors.

    :param player_choice: a string that represents the player's choice.
    :param computer_choice: a string that represents the computer's choice.
    :precondition: both arguments provided are "rock", "paper", or "scissors"
    :postcondition: return a string that declares if the player has won or not.
    :return: a string that declares whether the player won.

    >>> rock_paper_scissors_round("rock", "scissors")
    'You win!'
    >>> rock_paper_scissors_round("paper", "paper")
    "You don't win."
    """
    if (computer_choice == "rock" and player_choice == "paper") or \
       (computer_choice == "paper" and player_choice == "scissors") or \
       (computer_choice == "scissors" and player_choice == "rock"):
        return "You win!"
    else:
        return "You don't win."


def number_generator():
    """
    Generate a list of six random, unique integers in the range of [1, 49].

    Components of computational thinking:
    I demonstrated abstraction and generalization by using a helper function that allowed for greater customization
    than the problem calls for. It accepts a list of numbers, a minimum range parameter, a maximum range parameter,
    and a numbers parameter. This means that you can ask something like 55 random integers in the range [-442,
    999] and give the function some integers that you want the list to have.

    :return: a list of six random, unique integers in the range [1, 49].
    """
    return random_int_list_generator([], 1, 49, 6)


def random_int_list_generator(numbers_list, minimum_range, maximum_range, numbers):
    """
    Add random unique integers in the range [1, 49] to a given list until there are six unique integers in the range
    [1, 49] and return it.

    :param numbers_list: a list of unique integers in the range of [minimum_range, maximum_range] with no more
    objects than the parameter numbers.
    :param minimum_range: an integer representing the smallest int possible to generate.
    :param maximum_range: an integer greater than minimum_range + numbers, representing the largest int possible to
    generate.
    :param numbers: an integer representing the number of integers to generate.
    :precondition: the user must enter a valid argument according to the PARAM statement above.
    :postcondition: return a list of unique integers
    :return: a list of unique integers

    >>> random_int_list_generator([1, 2, 3, 4, 5, 6], 1, 49, 6)
    [1, 2, 3, 4, 5, 6]
    """
    new_number = random.randint(minimum_range, maximum_range)
    if len(numbers_list) < numbers:
        if new_number in numbers_list:
            return random_int_list_generator(numbers_list, minimum_range, maximum_range, numbers)
        else:
            numbers_list.append(new_number)
            return random_int_list_generator(numbers_list, minimum_range, maximum_range, numbers)
    else:
        numbers_list.sort()
        return numbers_list


def number_translator():
    """
    Translate the letters in a phone number to their numerical equivalent.

    :precondition: provide a string that represents a phone number in the format "XXX-XXX-XXXX" where any "X" can be
    a letter or number as an input.
    :postcondition: return a translated phone number as a string in the same format except all letters are now numbers.
    :return: return the translated phone number.
    """
    phone_number_input = input('Please enter a phone number in the format "XXX-XXX-XXXX".').upper()
    translated_number = ""
    for i in range(12):
        translated_number += translate_char(phone_number_input[i])
    return translated_number


def translate_char(char):
    """
    Translate a character to it's phone-book equivalent if the digit is a letter and return it, otherwise return the
    character.

    :param char: a string with a value that is equal to an uppercase letter.
    :precondition: the user must enter a valid argument according to the PARAM statement above.
    :postcondition: return an object defined below in the RETURN statement.
    :return: a string whose value is the translated digit or the string that was given as an argument.

    >>> translate_char("A")
    '2'
    >>> translate_char("4")
    '4'
    >>> translate_char("-")
    '-'
    """
    if char == "A" or char == "B" or char == "C":
        return "2"
    elif char == "D" or char == "E" or char == "F":
        return "3"
    elif char == "G" or char == "H" or char == "I":
        return "4"
    elif char == "J" or char == "K" or char == "L":
        return "5"
    elif char == "M" or char == "N" or char == "O":
        return "6"
    elif char == "P" or char == "Q" or char == "R" or char == "S":
        return "7"
    elif char == "T" or char == "U" or char == "V":
        return "8"
    elif char == "W" or char == "X" or char == "Y" or char == "Z":
        return "9"
    else:
        return char


def main():
    doctest.testmod()
    print(convert_to_roman_numeral(3313))
    colour_mixer()
    time_calculator(94553)
    print(compound_interest(100, 0.02, 2, 10))
    rock_paper_scissors()
    print(number_generator())
    print(number_translator())


if __name__ == "__main__":
    main()
