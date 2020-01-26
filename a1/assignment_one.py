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

    Prompt the user for two inputs. If the entered inputs are not both primary colours, print a useful error message. If
    the inputs are primary colours but they are the same, print a useful error message. Otherwise print the correct
    colour.
    :postcondition: print either an error message if the inputs are not strings with the value of two different
    primary colours, or the resulting secondary colour if inputs are two different primary colours.
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

    >>> time_calculator(95862)
    1 2 37 42
    >>> time_calculator(3606)
    0 1 0 6
    """
    print(time_converter(seconds, 0, 0, 0))


def time_converter(seconds, days, hours, minutes):
    """
    Simplify time in days, hours, minutes, and seconds.

    Given days, hours, minutes, and seconds, return time in the same format in such a way where seconds are converted
    into the largest units of time possible. It is possible that the time returned will not be completely simplified
    if parameters are given in such a way that produce more minutes or hours than than 59. This only occurs if:
    (seconds % 86400) // 3600 + hours >= 60 or (seconds % 3600) // 60 + minutes >= 60. This will never occur if the
    arguments provided for the hours and minutes are 0.
    :param seconds: a non-negative integer representing seconds.
    :param days: a non-negative integer representing days.
    :param hours: a non-negative integer representing hours.
    :param minutes: a non-negative integer representing minutes.
    :precondition: the user must enter valid arguments according to the PARAM statements above
    :postcondition: the function will return an object according to the return statement below, where the seconds
    given will be simplified into the largest units of time possible.
    :return: a string representing time in days, hours, minutes, and seconds as integers separated by a space (" ").

    >>> time_converter(90061, 0, 0, 0)
    '1 1 1 1'
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
    new_balance = principal * pow((1 + annual_interest/compound_frequency), (compound_frequency * time_years))
    return new_balance


def rock_paper_scissors():
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
    return random_int_list_generator([])


def random_int_list_generator(numbers_list):
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
    phone_number_input = input('Please enter a phone number in the format "XXX-XXX-XXXX".').upper()
    translated_number = ""
    for i in range(12):
        translated_number += translate_digit(phone_number_input[i])
    return translated_number


def translate_digit(digit):
    if digit.isnumeric():
        return digit
    elif digit == "A" or digit == "B" or digit == "C":
        return "2"
    elif digit == "D" or digit == "E" or digit == "F":
        return "3"
    elif digit == "G" or digit == "H" or digit == "I":
        return "4"
    elif digit == "J" or digit == "K" or digit == "L":
        return "5"
    elif digit == "M" or digit == "N" or digit == "O":
        return "6"
    elif digit == "P" or digit == "Q" or digit == "R" or digit == "S":
        return "7"
    elif digit == "T" or digit == "U" or digit == "V":
        return "8"
    elif digit == "W" or digit == "X" or digit == "Y" or digit == "Z":
        return "9"
    else:
        return "-"


def main():
    print(convert_to_roman_numeral(3313))
    colour_mixer()
    time_calculator(94553)
    print(compound_interest(100, 0.02, 2, 10))
    rock_paper_scissors()
    print(number_generator())
    print(number_translator())


if __name__ == "__main__":
    doctest.testmod()
    main()
