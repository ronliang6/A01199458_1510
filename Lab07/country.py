import doctest


class Country:
    """A simplified representation of a country."""
    def __init__(self, name: str, population: int, area: int):
        """
        Instantiate a country object with a name, population, and area.

        :param name: a string.
        :param population: a positive integer.
        :param area: a positive integer.
        :precondition: provide the function with valid arguments according to the PARAM statements above.
        :postcondition: instantiate a Country object with instance variables initialized according to the arguments
        provided.
        """
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, country):
        """
        Determine if this country has greater area than the country provided as the argument country.

        :param country: a country object.
        :precondition: provide the function with a valid argument according to the PARAM statement above.
        :postcondition: return an object as defined by the return statement below.
        :return: a bool.

        >>> america = Country("America", "1000", "3000")
        >>> canada = Country("Canada eh", "1000", "5000")
        >>> japan = Country("Japan", "1000", "3000")
        >>> canada.is_larger(america)
        True
        >>> america.is_larger(canada)
        False
        >>> america.is_larger(japan)
        False
        """
        return self.area > country.area

    def population_density(self):
        pass


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()