"""
Sort a list of colours into the order red, white, and blue.
"""

import doctest


def dijkstra(colour_list):
    """
    Sort a list of red, white, or blue.

    :param colour_list: a list of strings that only contain the values "red", "white", or "blue".
    :precondition: the function is called with acceptable PARAM statements as defined above.
    :postcondition: sort the list given into the order of red, then white, then blue.

    >>> dutch = ["red", "blue", "red"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'red', 'blue']
    >>> dutch = ["red"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red']
    >>> dutch = ["white", "red", "blue", "white", "red", "blue", "red", "blue", "white"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'red', 'red', 'white', 'white', 'white', 'blue', 'blue', 'blue']
    >>> dutch = (["red", "white", "blue"])
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'white', 'blue']
    """
    colour_list.sort(key=dutch_sort)


def dutch_sort(colour):
    """
    Assign a value to certain colours.

    :param colour: a string that has the value "red", "white", or "blue".
    :precondition: the function is called with acceptable PARAM statements as defined above.
    :postcondition: return an object defined below in the RETURN statement.
    :return: return an integer representing the value of the string given as an argument.

    >>> dutch_sort("red")
    1
    >>> dutch_sort("white")
    2
    >>> dutch_sort("blue")
    3
    """
    if colour == "red":
        return 1
    if colour == "white":
        return 2
    if colour == "blue":
        return 3


def main():
    doctest.testmod()
    dutch = ["white", "red", "blue", "white", "red", "blue", "red", "blue", "white"]
    dijkstra(dutch)
    print(dutch)


if __name__ == "__main__":
    main()