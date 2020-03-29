import io
from unittest import TestCase
from unittest.mock import patch
import tree


class TestTree(TestCase):
    def setUp(self):
        self.tree_one = tree.Tree("Doug-fir", 20, 100.4)

    def test_tree_init_species_empty_string(self):
        with self.assertRaises(ValueError):
            my_tree = tree.Tree("", 10, 100.0)

    def test_tree_init_species_white_spaces(self):
        with self.assertRaises(ValueError):
            my_tree = tree.Tree("   ", 10, 100.0)

    def test_tree_init_age_negative(self):
        with self.assertRaises(ValueError):
            my_tree = tree.Tree("Maple", -10, 100.0)

    def test_tree_init_circumference_negative(self):
        with self.assertRaises(ValueError):
            my_tree = tree.Tree("Maple", 10, -100.0)

    def test_tree_get_species(self):
        actual = self.tree_one.get_species()
        expected = "Doug-fir"
        self.assertEqual(actual, expected)

    def test_tree_get_age_years(self):
        actual = self.tree_one.get_age_years()
        expected = 20
        self.assertEqual(actual, expected)

    def test_tree_get_circumference_cm(self):
        actual = self.tree_one.get_circumference_cm()
        expected = 100.4
        self.assertEqual(actual, expected)

    def test_tree_set_age_years_negative(self):
        with self.assertRaises(ValueError):
            self.tree_one.set_age_years(-4)

    def test_tree_set_age_years_positive(self):
        self.tree_one.set_age_years(10)
        actual = self.tree_one.get_age_years()
        expected = 10
        self.assertEqual(actual, expected)

    def test_tree_set_circumference_cm_negative(self):
        with self.assertRaises(ValueError):
            self.tree_one.set_circumference_cm(-4)

    def test_tree_set_circumference_cm_positive(self):
        self.tree_one.set_circumference_cm(10.0)
        actual = self.tree_one.get_circumference_cm()
        expected = 10.0
        self.assertEqual(actual, expected)

    def test_tree_str_by_invoke(self):
        actual = self.tree_one.__str__()
        expected = 'This Doug-fir is 20 years old and has a circumference of 100.40 cm.'
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tree_str_by_print(self, output):
        print(self.tree_one)
        expected = 'This Doug-fir is 20 years old and has a circumference of 100.40 cm.\n'
        self.assertEqual(output.getvalue(), expected)

    def test_tree_repr_by_invoke(self):
        actual = self.tree_one.__repr__()
        expected = 'Tree("Doug-fir", 20, 100.4)'
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tree_repr_by_call_object(self, output):
        print(repr(self.tree_one))
        expected = 'Tree("Doug-fir", 20, 100.4)\n'
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tree_repr_by_call_collection_with_object(self, output):
        print(repr([self.tree_one]))
        expected = '[Tree("Doug-fir", 20, 100.4)]\n'
        self.assertEqual(output.getvalue(), expected)
