import io
from unittest import TestCase
from unittest.mock import patch
import country


class TestCountry(TestCase):
    def setUp(self):
        self.test_country = country.Country("America", 5000, 5000)
        self.test_country_2 = country.Country("Canada", 12000, 60)
        self.test_country_3 = country.Country("Japan", 20, 60)

    def test_is_larger_larger(self):
        actual = self.test_country.is_larger(self.test_country_2)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_larger_smaller(self):
        actual = self.test_country_2.is_larger(self.test_country)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_larger_equal(self):
        actual = self.test_country_2.is_larger(self.test_country_3)
        expected = False
        self.assertEqual(actual, expected)

    def test_population_density_one(self):
        actual = self.test_country.population_density()
        expected = 1.0
        self.assertEqual(actual, expected)

    def test_population_density_high(self):
        actual = self.test_country_2.population_density()
        expected = 200.0
        self.assertEqual(actual, expected)

    def test_population_density_low(self):
        actual = self.test_country_3.population_density()
        expected = 0.3333333333333333
        self.assertEqual(actual, expected)

    def test_str_by_invoke(self):
        actual = self.test_country.__str__()
        expected = 'America has a population of 5000 and is 5000 square kilometres.'
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_str_by_print(self, output):
        print(self.test_country)
        expected = 'America has a population of 5000 and is 5000 square kilometres.\n'
        self.assertEqual(output.getvalue(), expected)

    def test_repr_by_invoke(self):
        actual = self.test_country.__repr__()
        expected = "Country(\"America\", 5000, 5000)"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_repr_by_call_object(self, output):
        print(repr(self.test_country))
        expected = "Country(\"America\", 5000, 5000)\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_repr_by_call_collection_with_object(self, output):
        print(repr([self.test_country]))
        expected = "[Country(\"America\", 5000, 5000)]\n"
        self.assertEqual(output.getvalue(), expected)
