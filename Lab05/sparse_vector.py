import doctest


def sparse_add(vector1: dict, vector2: dict) -> dict:
    pass


def sparse_dot_product(vector1: dict, vector2: dict) -> int:
    pass


def sparse_vector_to_list(vector: dict) -> list:
    """

    :param vector:
    :return:

    >>> sparse_vector_to_list({0:1, 7:2, 9:11, 10:1, 12:1})
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 11, 1, 0, 1]

    """
    index = 0
    dict_as_list = []
    for key in vector:
        while key != index:
            dict_as_list.append(0)
            index += 1
        dict_as_list.append(vector[key])
        index += 1
    return dict_as_list


def main():
    doctest.testmod()
    pass


if __name__ == "__main__":
    main()
