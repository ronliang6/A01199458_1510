"""
Provide statistics on a provided list.
"""

import doctest


def statistics(stats_list):
    """
    Return a variety of statistics about a given list of numbers.

    The statistics returned include the number of elements in the list, the minimum value in that list, the maximum
    value in that list, the average value in that list, and the range of the list (the difference between the maximum
    and minimum.)
    :param stats_list: a list that contains zero or more integers and floats.
    :precondition: provide valid arguments according to the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a list of five floats that represent statistics about the given list.

    >>> statistics([-1.2, 56, -24, 1.1, 0])
    [5.0, -24.0, 56.0, 6.38, 80.0]
    >>> statistics([0])
    [1.0, 0.0, 0.0, 0.0, 0.0]
    >>> statistics([-1.75, -332, -23, -4.122, -45, -6, -7])
    [7.0, -332.0, -1.75, -59.838857142857144, 330.25]
    >>> statistics([1, 2.2, 2.8, 3.5, 5.5, 6, 7])
    [7.0, 1.0, 7.0, 4.0, 6.0]
    >>> statistics([])
    []
    """

    if len(stats_list) == 0:
        return []
    else:
        return_list = [0, 0, 0, 0, 0]
        return_list[0] = float(len(stats_list))

        min_value = stats_list[0]
        for i in range(len(stats_list)):
            if stats_list[i] < min_value:
                min_value = stats_list[i]
        return_list[1] = float(min_value)

        max_value = stats_list[0]
        for i in range(len(stats_list)):
            if stats_list[i] > max_value:
                max_value = stats_list[i]
        return_list[2] = float(max_value)

        running_sum = 0
        for i in range(len(stats_list)):
            running_sum += stats_list[i]
        list_average = running_sum / len(stats_list)
        return_list[3] = float(list_average)

        list_range = max_value - min_value
        return_list[4] = float(list_range)
        return return_list


def main():
    """Run doctests on the functions in this module."""
    doctest.testmod()


if __name__ == "__main__":
    main()
