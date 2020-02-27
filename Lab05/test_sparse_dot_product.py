from unittest import TestCase

import sparse_vector


class Test(TestCase):
    def test_sparse_dot_product_random_order_keys(self):
        actual = sparse_vector.sparse_dot_product({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
        expected = 30
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_only_zeroes(self):
        actual = sparse_vector.sparse_dot_product({'length': 5}, {'length': 5})
        expected = 0
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_length_zero(self):
        actual = sparse_vector.sparse_dot_product({'length': 0}, {'length': 0})
        expected = 0
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_length_one(self):
        actual = sparse_vector.sparse_dot_product({'length': 1, 0: 7}, {'length': 1, 0: -2})
        expected = -14
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_different_lengths(self):
        actual = sparse_vector.sparse_dot_product({'length': 1, 0: 7}, {'length': 2, 0: -2})
        expected = None
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_one_all_zeroes(self):
        actual = sparse_vector.sparse_dot_product({'length': 3, 0: 2, 2: 7}, {'length': 3})
        expected = 0
        self.assertEqual(actual, expected)
