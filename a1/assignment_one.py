import random
import doctest


def convert_to_roman_numeral(positive_int):
    """
    Translate a positive integer from decimal to roman numeral.

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

    The parameter position declares the reverse of the position of the positive_int to be translated. The value 0,
    will represent the last digit of the positive_int (the one's position) and the value 1 will represent the second
    last digit of the positive_int (the ten's position) and so forth.
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

    Prompt the user for two inputs for mixing primary colours. If the user enters invalid
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
    if (first_colour == "yellow" or first_colour == "blue") and (second_colour == "yellow" or second_colour == "blue"):
        return "green"
    if (first_colour == "blue" or first_colour == "red") and (second_colour == "blue" or second_colour == "red"):
        return "purple"


def time_calculator(seconds):
    """
    Convert time in seconds to time in days, hours, minutes, and seconds.

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

    :precondition: provide an input.
    :postcondition: a string that is an error message if they have entered an invalid input or one that informs the
    user whether they have won.
    """
    raw_input = input('Please enter "rock", "paper", or "scissors" to play this game.')
    player_choice = raw_input.strip().lower()
    if player_choice != "rock" and player_choice != "paper" and player_choice != "scissor":
        print('You have entered an invalid choice. The acceptable choices are "rock", "paper", or "scissors".')
    else:
        outcome = "don't win."
        random_number = random.randint(0, 2)
        if random_number == 0:
            computer_choice = "rock"
            if player_choice == "paper":
                outcome = "win."
        elif random_number == 1:
            computer_choice = "paper"
            if player_choice == "scissors":
                outcome = "win."
        else:
            computer_choice = "scissors"
            if player_choice == "rock":
                outcome = "win."
        print("The computer picked " + computer_choice + ". You picked " + player_choice + ". You " + outcome)


def number_generator():
    """
    Generate a list of six random, unique integers in the range of [1, 49].

    :return: a list of six random, unique integers in the range [1, 49].
    """
    return random_int_list_generator([])


def random_int_list_generator(numbers_list):
    """
    Add random unique integers in the range [1, 49] to a given list until there are six unique integers in the range
    [1, 49] and return it.

    :param numbers_list: a list of unique integers in the range [1, 49] with no more than 6 objects.
    :precondition: the user must enter a valid argument according to the PARAM statement above.
    :postcondition: return a list of six unique integers in the range [1, 49].
    :return: a list of six unique integers in the range [1, 49].

    >>> random_int_list_generator([1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    """
    new_number = random.randint(1, 49)
    if len(numbers_list) <= 5:
        if new_number in numbers_list:
            return random_int_list_generator(numbers_list)
        else:
            numbers_list.append(new_number)
            return random_int_list_generator(numbers_list)
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
