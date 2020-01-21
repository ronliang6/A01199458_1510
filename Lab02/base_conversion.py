def calculate_new_number():
    """Convert a base 10 number to another base in the range [2, 9].

    Takes in an input as the destination base and calculates the maximum base-10 number possible to convert. Also
    takes in an input as a base ten number that will be converted to a 4bit number of the destination base. Call
    calculate_digit to calculate the remainder, then format and insert that digit as the first index of a
    list. Call calculate_quotient to calculate the quotient to continue calculating the next digits. Repeat until
    four digits have been entered into the list. Concatenate each digit in list into the new number and return it.
    """

    destination_base = int(input("Please enter the base destination, a number between 2 and 9, inclusive"))
    maximum_base10_number = pow(destination_base, 4) - 1
    print("The maximum base 10 number that can be converted is " + str(maximum_base10_number))
    number_to_convert = int(input("Please enter a number that is less than or equal to " + str(maximum_base10_number)))

    digits_list = []

    digit_first = calculate_digit(number_to_convert, destination_base)
    digits_list.insert(0, str(digit_first))
    quotient_first = calculate_quotient(number_to_convert, destination_base)
    digit_second = calculate_digit(quotient_first, destination_base)
    digits_list.insert(0, str(digit_second))
    quotient_second = calculate_quotient(quotient_first, destination_base)
    digit_third = calculate_digit(quotient_second, destination_base)
    digits_list.insert(0, str(digit_third))
    quotient_third = calculate_quotient(quotient_second, destination_base)
    digit_fourth = calculate_digit(quotient_third, destination_base)
    digits_list.insert(0, str(digit_fourth))

    number_in_new_base = "".join(digits_list)

    return number_in_new_base


def calculate_digit(dividend, divisor):
    """Calculate the modulus of two numbers."""
    return dividend % divisor


def calculate_quotient(dividend, divisor):
    """Calculate the quotient of two numbers."""
    return dividend // divisor


def main():
    """Call and print the calculate_new_number function."""

    print(calculate_new_number())


if __name__ == "__main__":
    """Call the main method if this is the main program."""

    main()
