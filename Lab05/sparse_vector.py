import doctest


def sparse_add(vector1: dict, vector2: dict):
    """
    Add two sparse vectors formatted at dictionaries if their lengths are the same.

    This function will return None if the lengths are not the same.
    :param vector1: A dictionary representing a sparse vector.
    :param vector2: A dictionary representing a sparse vector.
    :precondition: The dictionary parameters above must contain a key 'length' with an integer value.
    :postcondition: The function will return an object as defined by the return statement below.
    :return: Return None if the sparse vector lengths are not equal, or the sum of the vectors as a dictionary
    representing a sparse vector if they are.
    >>> sparse_add({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
    {0: 4.3, 2: 7.5, 4: -11, 'length': 5}
    >>> sparse_add({2: 2, 'length': 13, 5: 1, 6: 12, 9: 1}, {2: 1, 'length': 12, 7: 7, 9: 1})

    >>> sparse_add({'length': 5}, {'length':5})
    {'length': 5}
    """
    if vector1['length'] != vector2['length']:
        return None
    length = vector1['length']
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
    Calculate and return the dot product of two vectors.

    The dot product of two vectors is calculated as the sum of the element-wise products of the vectors' elements.
    :param vector1: A dictionary representing a sparse vector.
    :param vector2: A dictionary representing a sparse vector.
    :precondition: The dictionary parameters above must contain a key 'length' with an integer value.
    :postcondition: The function will return an object as defined by the return statement below.
    :return: Return None if the sparse vector lengths are not equal, or an integer representing the dot product of
    the two vectors given as arguments if the lengths are equal.
    >>> sparse_dot_product({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
    30.0
    >>> sparse_dot_product({2: 18, 'length': 12, 5: 4, 6: 12, 9: 1}, {2: 1, 7: 7, 'length': 10, 9: 3})

    >>> sparse_dot_product({'length': 5}, {'length':5})
    0
    """
    if vector1['length'] != vector2['length']:
        return None
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
    Translate a sparse vector given as a dictionary to a list.

    :param vector: A dictionary representing a sparse vector.
    :precondition: Provide the function with valid arguments as defined by the PARAM statement above.
    :postcondition: Return an object as defined by the return statement below.
    :return: A list of floats representing a sparse vector.

    >>> sparse_vector_to_list({7: 2, 0: 1.01, 9: 11, 'length': 14, 10: 1, 12: 1.77})
    [1.01, 0, 0, 0, 0, 0, 0, 2, 0, 11, 1, 0, 1.77, 0]
    >>> sparse_vector_to_list({'length': 5})
    [0, 0, 0, 0, 0]
    """
    dict_as_list = []
    for _ in range(vector['length']):
        dict_as_list.append(0)
    del vector['length']
    for key in vector:
        dict_as_list[key] = vector[key]
    return dict_as_list


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
