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