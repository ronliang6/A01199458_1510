import doctest


def sparse_add(vector1: dict, vector2: dict):
    """

    :param vector1:
    :param vector2:
    :return:
    >>> sparse_add({2:2, 'length': 12, 5:1, 6:12, 9:1}, {2:1, 'length': 12, 7:7, 9:1})
    {2: 3, 5: 1, 6: 12, 7: 7, 9: 2, 'length': 12}
    >>> sparse_add({2:2, 'length': 13, 5:1, 6:12, 9:1}, {2:1, 'length': 12, 7:7, 9:1})

    """
    if vector1['length'] != vector2['length']:
        return None
    length = vector1['length']
    del vector1['length']
    del vector2['length']
    vector1_as_list = sparse_vector_to_list(vector1)
    vector2_as_list = sparse_vector_to_list(vector2)
    vector_sum_list = []
    vector_sum_dict = {}

    for i in range(len(vector1_as_list)):
        vector_sum_list.append(vector1_as_list[i] + vector2_as_list[i])
    for item in enumerate(vector_sum_list):
        if item[1] != 0:
            vector_sum_dict[item[0]] = item[1]
    vector_sum_dict['length'] = length

    return vector_sum_dict


def sparse_dot_product(vector1: dict, vector2: dict):
    """

    :param vector1:
    :param vector2:
    :return:
    >>> sparse_dot_product({2:2, 5:1, 'length': 15, 6:12, 9:1}, {2:1, 'length': 15, 7:7, 9:1})
    3
    >>> sparse_dot_product({2:18, 5:4, 'length': 12, 6:12, 9:1}, {2:1, 'length': 12, 7:7, 9:3})
    21
    >>> sparse_dot_product({2:18, 'length': 12, 5:4, 6:12, 9:1}, {2:1, 7:7, 'length': 10, 9:3})

    """
    if vector1['length'] != vector2['length']:
        return None
    del vector1['length']
    del vector2['length']
    vector1_as_list = sparse_vector_to_list(vector1)
    vector2_as_list = sparse_vector_to_list(vector2)
    vector_product_list = []
    products_sum = 0
    for i in range(len(vector1_as_list)):
        vector_product_list.append(vector1_as_list[i] * vector2_as_list[i])
    for integer in vector_product_list:
        products_sum += integer
    return products_sum


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
