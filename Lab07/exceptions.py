import doctest


def heron(num: int):
    """
    Return the square root of a given integer or -1 if that integer is not positive.

    :param num: an integer.
    :precondition: provide the function with a valid argument according to the PARAM statement above.
    :postcondition: return an object according to the return statement below. If num is 0 or negative,
    print a helpful warning message.
    :raise ZeroDivisionError: if PARAM num is 0 or negative.
    :return: a float that represents the square root of num with two or less decimal places or -1 if num is 0 or
    negative.

    >>> heron(0)
    0.0
    >>> heron(-50)
    You have entered a negative integer, that is not valid.
    -1
    >>> heron(1)
    1.0
    >>> heron(0.25)
    0.5
    >>> heron(1000)
    31.62
    >>> heron(10000)
    100.0
    """
    try:
        if num < 0:
            raise ZeroDivisionError
        else:
            guess = num
            tolerance = 0.00001
            while abs(guess * guess - num) > tolerance:  # continue finding a more accurate guess if the guess is not
                # close enough to the true root, as defined by the tolerance
                guess = (guess + num / guess) / 2  # this formula is a step towards finding the square root of a number
            return float(round(guess, 2))
    except ZeroDivisionError:
        print("You have entered a negative integer, that is not valid.")
        return -1


def find_an_even(input_list: list):
    """
    Return the first even number in input_list.

    :param input_list: a list of integers.
    :precondition: input_list must be a list of integer.
    :postcondition: return the first even number in input_list.
    :raise ValueError: if input_list does not contain an even number.
    :return: first even number in input_list.

    >>> find_an_even([0])
    0
    >>> find_an_even([0, 2])
    0
    >>> find_an_even([1, 9, 0])
    0
    """

    for integer in input_list:
        if integer % 2 == 0:
            return integer
    raise ValueError


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
