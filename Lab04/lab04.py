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
    >>> eratosthenes(2)
    [2]
    >>> eratosthenes(10)
    [2, 3, 5, 7]
    >>> eratosthenes(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    numbers_list = list(range(2, upperbound + 1))
    position = 0

    if upperbound > 2:
        while numbers_list[position] < math.sqrt(upperbound):
            numbers_list = delete_multiples_of(numbers_list, numbers_list[position])
            position += 1

    return numbers_list


def delete_multiples_of(numbers_list, number):
    """
    Delete all multiples of a number in a list except that number itself.

    :param numbers_list: A list of one or more positive integers.
    :param number: A positive integer.
    :precondition: provide the function with valid arguments as defined by the PARAM statements above.
    :postcondition: return an object as defined by the return statement below.
    :return: A list with zero or more positive integers.

    >>> delete_multiples_of([1], 1)
    [1]
    >>> delete_multiples_of([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    [1, 2, 3, 5, 7, 9]
    >>> delete_multiples_of([1, 4, 7, 12], 72)
    [1, 4, 7, 12]
    >>> delete_multiples_of([2, 6, 7, 212], 5)
    [2, 6, 7, 212]
    >>> delete_multiples_of([10, 15, 20, 25], 5)
    []
    """
    numbers_to_delete = []

    for i in range(len(numbers_list)):
        # For each integer in the list that is divisible by prime but is not prime, add that integer to a list
        if numbers_list[i] % number == 0 and numbers_list[i] != number:
            numbers_to_delete.append(numbers_list[i])

    for i in range(len(numbers_to_delete)):
        numbers_list.remove(numbers_to_delete[i])
    return numbers_list


def cash_money(money):
    """
    Calculate the largest denominations of bills and coins that can represent the money inputted as a float.

    :param money: A positive float with with no more than two decimal places.
    :precondition: Provide the function with a valid argument as defined by the PARAM statement above.
    :postcondition: Return an object as defined by the return statement below.
    :return: A list of eleven integers representing the number of each denomination.

    >>> cash_money(0.00)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> cash_money(0.01)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    >>> cash_money(0.02)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
    >>> cash_money(0.05)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    >>> cash_money(0.10)
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    >>> cash_money(0.25)
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    >>> cash_money(1.00)
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    >>> cash_money(1.05)
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    >>> cash_money(2.00)
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    >>> cash_money(5.00)
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    >>> cash_money(10.00)
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    >>> cash_money(10.27)
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2]
    >>> cash_money(20.00)
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> cash_money(50.00)
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> cash_money(100.00)
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> cash_money(100.57)
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 2]
    >>> cash_money(188.41)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    money *= 100
    denominations = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
    breakdown = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(denominations)):
        if money >= denominations[i]*100:
            breakdown[i] = int(money // (denominations[i]*100))
            money %= denominations[i]*100
    return breakdown


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
