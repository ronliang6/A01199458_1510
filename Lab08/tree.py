import doctest


class Tree:
    """A simplified representation of a tree."""
    def __init__(self, species: str, age_years: int, circumference_cm: float):
        """
        Instantiate a tree object with its species, age (years), and trunk circumference (centimeters).

        :param species: a string.
        :param age_years: an integer.
        :param circumference_cm: a float.
        :precondition: provide the function with valid arguments as defined by the PARAM statements above.
        :postcondition: instantiate a Tree object with instance variables initialized according to the arguments
        provided.
        :raise ValueError: if species does not contain at least one non-whitespace character, or if age_years is
        negative, or if circumference_cm is negative.
        """
        if species.replace(" ", ""):
            self.__species = species
        else:
            raise ValueError("species requires at least one non-whitespace character.")
        if age_years >= 0:
            self.__age_years = age_years
        else:
            raise ValueError("age_years must be at least 0.")
        if circumference_cm >= 0:
            self.__circumference_cm = circumference_cm
        else:
            raise ValueError("circumference_cm must be at least 0.")

    def get_species(self) -> str:
        """
        Return the tree species as a string.

        :precondition: provide the function with no arguments.
        :postcondition: return an object as defined by the return statement below.
        :return: a string representing the tree species.

        >>> tree_one = Tree("Douglas-fir", 20, 31.23)
        >>> tree_one.get_species()
        'Douglas-fir'
        """
        return self.__species

    def get_age_years(self) -> int:
        """
        Return the tree age in years as an int.

        :precondition: provide the function with no arguments.
        :postcondition: return an object as defined by the return statement below.
        :return: an int representing the tree age in years.

        >>> tree_one = Tree("Douglas-fir", 20, 31.23)
        >>> tree_one.get_age_years()
        20
        """
        return self.__age_years

    def get_circumference_cm(self) -> float:
        """
        Return the tree circumference in cm as a float.

        :precondition: provide the function with no arguments.
        :postcondition: return an object as defined by the return statement below.
        :return: a float representing the tree circumference in cm.

        >>> tree_one = Tree("Douglas-fir", 20, 31.23)
        >>> tree_one.get_circumference_cm()
        31.23
        """
        return self.__circumference_cm

    def set_species(self, species: str):
        if species.replace(" ", ""):
            self.__species = species
        else:
            raise ValueError("species requires at least one non-whitespace character.")

    def set_age_years(self, age_years: int):
        if age_years >= 0:
            self.__age_years = age_years
        else:
            raise ValueError("age_years must be at least 0.")

    def set_circumference_cm(self, circumference_cm: float):
        if circumference_cm >= 0:
            self.__circumference_cm = circumference_cm
        else:
            raise ValueError("circumference_cm must be at least 0.")

    def __str__(self) -> str:
        """
        Return a string that describes a tree.

        This function also changes the way the print() function works. When a Tree object is passed to a print()
        function, that function will instead print the string returned by this function.

        :precondition: provide the function with no arguments.
        :postcondition: return an object as defined by the return statement below.
        :return: a string describing a tree.
        """


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()