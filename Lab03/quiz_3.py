"""
Solve a variety of problems.
Ronald Liang
A01199458

Partner: Kyrill Metalnikov
"""


import doctest


def average_three_greatest_ints(int1, int2, int3, int4):
    """
    Calculate the average of the three greatest integers when given four.

    :param int1: an integer that represents a grade.
    :param int2: an integer that represents a grade.
    :param int3: an integer that represents a grade.
    :param int4: an integer that represents a grade.
    :precondition: provide acceptable arguments according to the PARAM statements above.
    :postcondition: return an object according to the return value below.
    :return: a float that represents the average of the three highest grades.

    >>> average_three_greatest_ints(1, 2, 3, 4)
    3.0
    >>> average_three_greatest_ints(0, 0, 0, 0)
    0.0
    >>> average_three_greatest_ints(1000, 7000, 9000, 14000)
    10000.0
    """
    grades_list = [int1, int2, int3, int4]
    grades_list.sort()
    return (grades_list[1] + grades_list[2] + grades_list[3])/3


def index_of_substring(sentence, substring):
    """
    Return the index of a substring in another string if that string contains the substring.

    :param sentence: a string.
    :param substring: a string.
    :precondition: valid arguments are provided as defined by the PARAM statements above.
    :postcondition: return -1 if the substring is not in the sentence and the index of the string if it is.
    :return: an integer that represents either the index of the substring or -1 if the substring is not in the sentence.

    >>> index_of_substring("0123456789", "4")
    4
    >>> index_of_substring("Hello how are you doing", "are")
    10
    >>> index_of_substring("", "")
    0
    """
    if substring in sentence:
        return sentence.find(substring)
    else:
        return -1


def main():
    """
    Manipulate a list in a variety of ways.
    """
    doctest.testmod()
    ids = [4353, 2314, 2956, 3382, 9362, 3900]
    ids.remove(3382)
    print(ids)
    id_9362 = ids.index(9362)
    print(ids)
    ids.insert(id_9362 + 1, 4499)
    print(ids)
    ids.append(5566)
    print(ids)
    ids.append(1830)
    print(ids)
    ids.reverse()
    print(ids)
    ids.sort()


if __name__ == "__main__":
    main()
