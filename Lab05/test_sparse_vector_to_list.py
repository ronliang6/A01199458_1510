from unittest import TestCase

import sparse_vector


class Test(TestCase):
    def test_sparse_vector_to_list_random_order_keys(self):
        actual = sparse_vector.sparse_vector_to_list({4: -5, 'length': 5, 0: 4.3})
        expected = [4.3, 0, 0, 0, -5]
        self.assertEqual(actual, expected)

    def test_sparse_vector_to_list_length_zero(self):
        actual = sparse_vector.sparse_vector_to_list({'length': 0})
        expected = []
        self.assertEqual(actual, expected)

    def test_sparse_vector_to_list_length_one(self):
        actual = sparse_vector.sparse_vector_to_list({0: 12, 'length': 1})
        expected = [12]
        self.assertEqual(actual, expected)

    def test_sparse_vector_to_list_only_zeroes(self):
        actual = sparse_vector.sparse_vector_to_list({'length': 12})
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)