def format_name(first_name, last_name):
    """Delete trailing/leading whitespace and title-cases two strings."""
    full_name = first_name.strip().title() + " " + last_name.strip().title()
    return full_name


def tripler(thing):
    """Repeat a string three times or multiples a number by three."""
    input_tripled = str(thing) * 3
    return input_tripled


def this_year():
    """"Calculate a surprising equation that resolves to 2020 and returns it."""
    surprising_math = int(2020 * 0 / 20 + 200 / 0.2 * 2 + 20)
    return surprising_math


def base_conversion():
    """Convert a base 10 number to another base, with bounds."""
    destination_base = int(input("Please enter the base destination, a number between 2 and 9, inclusive"))
    maximum_base10_number = pow(destination_base, 4) - 1
    print("The maximum base 10 number that can be converted is " + str(maximum_base10_number))
    number_to_convert = int(input("Please enter a number that is less than or equal to " + str(maximum_base10_number)))
    remainder_first = number_to_convert % destination_base
    quotient_first = number_to_convert // destination_base
    remainder_second = quotient_first % destination_base
    quotient_second = quotient_first // destination_base
    remainder_third = quotient_second % destination_base
    quotient_third = quotient_second // destination_base
    remainder_fourth = quotient_third % destination_base

    converted_number = int(str(remainder_fourth) + str(remainder_third) + str(remainder_second) + str(remainder_first))
    print(converted_number)


def main():
    """Invoke other functions and print results."""
    print(format_name("   RONALD   ", "   LIAng  "))
    print(tripler("3"))
    print(this_year())
    base_conversion()


if __name__ == "__main__":
    """Invoke the main function if this file is the main program."""
    main()

