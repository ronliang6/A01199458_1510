import doctest


class Country:
    """A simplified representation of a country."""
    def __init__(self, name: str, population: int, area: int):
        """
        Instantiate a country object with a name, population, and area.

        :param name: a string.
        :param population: an integer.
        :param area: an integer.
        :precondition: provide the function with valid arguments according to the PARAM statements above.
        :postcondition: instantiate a Country object with instance variables initialized according to the arguments
        provided.
        :raise ValueError: if the population or area is less than
        """

        if population <= 0 or area <= 0:
            raise ValueError("The population and area must be an integer greater than zero.")
        else:
            self.population = population
            self.area = area
        self.name = name

    def is_larger(self, country) -> bool:
        """
        Determine if this country has greater area than the country provided as the argument country.

        :param country: a country object.
        :precondition: provide the function with a valid argument according to the PARAM statement above.
        :postcondition: return an object as defined by the return statement below.
        :return: a bool.

        >>> america = Country("America", 1000, 3000)
        >>> canada = Country("Canada eh", 1000, 5000)
        >>> japan = Country("Japan", 1000, 3000)
        >>> canada.is_larger(america)
        True
        >>> america.is_larger(canada)
        False
        >>> america.is_larger(japan)
        False
        """
        return self.area > country.area

    def population_density(self) -> float:
        """
        Return the population density of a country.

        :precondition: provide the function with no arguments.
        :postcondition: return an object as defined by the return statement below.
        :return: a float representing the population density of a country.

        >>> america = Country("America", 100, 100)
        >>> japan = Country("Japan", 10000, 10)
        >>> canada = Country("Canada", 500, 50000)
        >>> america.population_density()
        1.0
        >>> japan.population_density()
        1000.0
        >>> canada.population_density()
        0.01
        """
        return self.population / self.area

    def __str__(self) -> str:
        """
        Return a string that describes a country.

        This function also changes the way the print() function works. When a Country object is passed to a print()
        function, that function will instead print the string returned by this function.

        :precondition: provide the function with no arguments.
        :postcondition: return an object as defined by the return statement below.
        :return: a string describing the country.

        >>> america = Country("America", 1000, 100000)
        >>> print(america)
        America has a population of 1000 and is 100000 square kilometres.
        >>> america.__str__()
        'America has a population of 1000 and is 100000 square kilometres.'
        """
        return self.name + " has a population of " + str(self.population) + " and is " + str(self.area) + " square " \
                                                                                                          "kilometres."

    def __repr__(self) -> str:
        """
        Return a string that represents the country object and it's instance variables.

        This function also modifies the way country objects are displayed in the shell or when a called as part of a
        collection. By default, it represents the object type and it's address in memory. Now it displays useful
        information about the object.

        :precondition: provide the function with no arguments.
        :postcondition: return an object as defined by the return statement below.
        :return: a string representing a country object.

        >>> america = Country("America", 51522, 222222)
        >>> america
        Country("America", 51522, 222222)
        >>> [america]
        [Country("America", 51522, 222222)]
        """
        return "Country(\"" + self.name + "\", " + str(self.population) + ", " + str(self.area) + ")"


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()