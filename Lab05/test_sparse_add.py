from unittest import TestCase
from unittest.mock import patch

import sparse_vector


class Test(TestCase):
    @patch('sparse_vector.sparse_vector_to_list', side_effect=[[0, 0, 0], [0, 0, 0]])
    def test_sparse_add_only_zeroes(self, _):
        actual = sparse_vector.sparse_add({'length': 3}, {'length': 3})
        expected = {'length': 3}
        self.assertEqual(actual, expected)

    @patch('sparse_vector.sparse_vector_to_list', side_effect=[[1, 2, 8], [0, 0, 0]])
    def test_sparse_add_one_all_zeroes(self, _):
        actual = sparse_vector.sparse_add({0: 1, 1: 2, 2: 8, 'length': 3}, {'length': 3})
        expected = {0: 1, 1: 2, 2: 8, 'length': 3}
        self.assertEqual(actual, expected)

    @patch('sparse_vector.sparse_vector_to_list', side_effect=[[], []])
    def test_sparse_add_length_zero(self, _):
        actual = sparse_vector.sparse_add({'length': 0}, {'length': 0})
        expected = {'length': 0}
        self.assertEqual(actual, expected)

    @patch('sparse_vector.sparse_vector_to_list', side_effect=[[0, 0, 7.5, 0, -6], [4.3, 0, 0, 0, -5]])
    def test_sparse_add_random_order_keys(self, _):
        actual = sparse_vector.sparse_add({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
        expected = {0: 4.3, 2: 7.5, 4: -11, 'length': 5}
        self.assertEqual(actual, expected)

    @patch('sparse_vector.sparse_vector_to_list', side_effect=[[2], [3]])
    def test_sparse_add_length_one(self, _):
        actual = sparse_vector.sparse_add({'length': 1, 0: 2}, {0: 3, 'length': 1})
        expected = {0: 5, 'length': 1}
        self.assertEqual(actual, expected)

    @patch('sparse_vector.sparse_vector_to_list', side_effect=[[-1, -2], [1, 2]])
    def test_sparse_add_complimentary_elements(self, _):
        actual = sparse_vector.sparse_add({'length': 2, 0: -1, 1: -2}, {0: 1, 'length': 2, 1: 2})
        expected = {'length': 2}
        self.assertEqual(actual, expected)

    def test_sparse_add_different_lengths(self):
        actual = sparse_vector.sparse_add({'length': 2, 0: 2}, {0: 3, 'length': 1})
        expected = None
        self.assertEqual(actual, expected)
