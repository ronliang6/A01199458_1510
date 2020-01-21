"""
Functions to convert a base 10 number to a number in a different base.
"""


def calculate_new_number():
    """Convert a base 10 number to another base in the range [2, 9].

    Given the number of bits and the destination base, the maximum base ten number is determined. Given a number no
    larger than the maximum number, the new number is calculated digit by digit and returned.

    :return: the converted number
    """

    destination_base = int(input("Please enter the base destination, a number between 2 and 9, inclusive"))
    bits = int(input("Please enter the number of bits you would like your answer in"))
    maximum_base10_number = maximum_number(destination_base, bits)
    print("The maximum base 10 number that can be converted is " + str(maximum_base10_number))
    number_to_convert = int(input("Please enter a number that is less than or equal to " + str(maximum_base10_number)))

    new_number = ""

    digit_first = calculate_digit(number_to_convert, destination_base)
    new_number = str(digit_first) + new_number
    quotient_first = calculate_quotient(number_to_convert, destination_base)
    digit_second = calculate_digit(quotient_first, destination_base)
    new_number = str(digit_second) + new_number
    quotient_second = calculate_quotient(quotient_first, destination_base)
    digit_third = calculate_digit(quotient_second, destination_base)
    new_number = str(digit_third) + new_number
    quotient_third = calculate_quotient(quotient_second, destination_base)
    digit_fourth = calculate_digit(quotient_third, destination_base)
    new_number = str(digit_fourth) + new_number

    return new_number


def calculate_digit(dividend, divisor):
    """Calculate the modulus of two numbers.

    :param dividend: a number
    :param divisor: a number
    :return: the result of dividend modulus divisor
    """

    return dividend % divisor


def maximum_number(destination_base, bits):
    """
    Calculate the maximum base 10 number that you can convert given the destination base and the number of bits.

    :param destination_base: a positive integer
    :param bits: a positive integer
    :return: a positive integer
    """

    return pow(destination_base, bits) - 1


def calculate_quotient(dividend, divisor):
    """Calculate the quotient of two numbers.

    :param dividend: a number
    :param divisor: a number
    :return: the result of dividend integer-division divisor
    """
    return dividend // divisor


def main():
    """Call and print the calculate_new_number function."""

    print(calculate_new_number())


if __name__ == "__main__":
    main()
