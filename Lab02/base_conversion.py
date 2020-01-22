"""
Functions to convert a base 10 number to a number in a different base.
"""


def base_conversion():
    """Convert a base 10 number to another base in the range [2, 9].

    Given the number of bits and the destination base, the maximum base ten number is determined. Given a number no
    larger than the maximum number, the new number is calculated digit by digit and returned.

    :return: the converted number as a string
    """

    destination_base = int(input("Please enter the base destination, a number between 2 and 9, inclusive"))
    maximum_base10_number = maximum_number(destination_base, 4)
    print("The maximum base 10 number that can be converted is " + str(maximum_base10_number))
    number_to_convert = int(input("Please enter a number that is less than or equal to " + str(maximum_base10_number)))

    digit_first = number_to_convert % destination_base
    quotient_first = number_to_convert // destination_base
    digit_second = quotient_first % destination_base
    quotient_second = quotient_first // destination_base
    digit_third = quotient_second % destination_base
    quotient_third = quotient_second // destination_base
    digit_fourth = quotient_third % destination_base

    new_number = str(digit_fourth) + str(digit_third) + str(digit_second) + str(digit_first)
    return new_number


def maximum_number(destination_base, bits):
    """
    Calculate the maximum base 10 number that you can convert given the destination base and the number of bits.

    :param destination_base: the destination base that the answer will be in as a positive integer
    :param bits: the number of bits that the answer will be in as a positive integer
    :return: the maximum base 10 number possible to convert as an integer
    """

    return pow(destination_base, bits) - 1


def main():
    """Call and print the base_conversion function."""

    print(base_conversion())


if __name__ == "__main__":
    main()
