import doctest
import math


def eratosthenes(upperbound):
    """

    :param upperbound: a positive integer
    :return:

    >>> eratosthenes(10)
    [2, 3, 5, 7]

    >>> eratosthenes(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    numbers_list = list(range(2, upperbound))
    position = 0

    while numbers_list[position] < math.sqrt(upperbound):
        numbers_list = eratosthenes_helper(numbers_list, numbers_list[position])
        position += 1

    return numbers_list


def eratosthenes_helper(numbers_list, prime):
    numbers_to_delete = []

    for i in range(len(numbers_list)):
        # For each integer in the list that is divisible by prime but is not prime, add that integer to a list
        if numbers_list[i] % prime == 0 and numbers_list[i] != prime:
            numbers_to_delete.append(numbers_list[i])

    for i in range(len(numbers_to_delete)):
        numbers_list.remove(numbers_to_delete[i])
    return numbers_list


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
