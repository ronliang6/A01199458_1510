import doctest
import math


def eratosthenes(upperbound):
    """
    Return a list of all prime numbers less than the upper bound provided.

    :param upperbound: A positive integer.
    :precondition: Enter valid arguments according to the PARAM statement above.
    :postcondition: Return a list of all the prime numbers less than the upperbound parameter.
    :return: A list of positive integers.

    >>> eratosthenes(1)
    []
    >>> eratosthenes(3)
    [2]
    >>> eratosthenes(10)
    [2, 3, 5, 7]
    >>> eratosthenes(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    numbers_list = list(range(2, upperbound))
    position = 0

    if upperbound > 2:
        while numbers_list[position] < math.sqrt(upperbound):
            numbers_list = delete_multiples_of(numbers_list, numbers_list[position])
            position += 1

    return numbers_list


def delete_multiples_of(numbers_list, prime):
    numbers_to_delete = []

    for i in range(len(numbers_list)):
        # For each integer in the list that is divisible by prime but is not prime, add that integer to a list
        if numbers_list[i] % prime == 0 and numbers_list[i] != prime:
            numbers_to_delete.append(numbers_list[i])

    for i in range(len(numbers_to_delete)):
        numbers_list.remove(numbers_to_delete[i])
    return numbers_list


def cash_money(money):
    """
    Calculate the largest denominations of bills and coins that can represent the money inputted as a float.

    :param money: A positive float.
    :precondition: Provide the function with a valid argument as defined by the PARAM statement above.
    :postcondition: Return an object as defined by the return statement below.
    :return: A list of eleven integers representing the number of each denomination.

    >>> cash_money(0.01)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    >>> cash_money(88.68)
    [0, 1, 1, 1, 1, 1, 1, 2, 1
    >>> cash_money(9999999.99)
    [99999, 1, 2, 0, 1, 2, 0, 3, 2, 0, 4]
    """
    denominations = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
    breakdown = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(denominations)):
        if money >= denominations[i]:
            breakdown[i] = int(money // denominations[i])
            money %= denominations[i]
    return breakdown


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
