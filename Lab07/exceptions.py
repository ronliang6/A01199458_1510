import doctest


def heron(num: int):
    """
    Return the square root of a given integer or -1 if that integer is not positive.

    :param num: an integer.
    :precondition: provide the function with a valid argument according to the PARAM statement above.
    :postcondition: return an object according to the return statement below. If num is 0 or negative,
    print a helpful warning message.
    :raise ZeroDivisionError: if PARAM num is 0 or negative.
    :return: a float that represents the square root of num with four or less decimal places or -1 if num is 0 or
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
    31.6228
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
            return float(round(guess, 4))
    except ZeroDivisionError:
        print("You have entered a negative integer, that is not valid.")
        return -1


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()