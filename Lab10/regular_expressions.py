import doctest
import re


def is_email(address: str) -> bool:
    """
    Determine if the given argument address matches an email format.

    The email format is defined below as a regex string. The last two to four characters of the email, the "top-level
    domain", can include white spaces.

    :param address: a string.
    :precondition: provide the function with an argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a bool that represents whether or not the provided string 'address' is a valid email address.

    >>> is_email("a@gmail.com")
    True
    >>> is_email("A@gmail.com")
    True
    >>> is_email("0@gmail.com")
    True
    >>> is_email("A010gsz@gmail.com")
    True
    >>> is_email("@gmail.com")
    False
    >>> is_email("a12rerR@gmailcom")
    False
    >>> is_email("a12rerR@gmail..com")
    True
    >>> is_email("a12rerR@gma.il.com")
    False
    >>> is_email("")
    False
    >>> is_email("!~@gmail.com")
    False
    >>> is_email("heela@gmail.comcom")
    False
    >>> is_email("a12rerR@gmail.p")
    False
    >>> is_email("hello bob@gmail.com")
    False
    >>> is_email("bob@gmail.com hello")
    False
    >>> is_email("hello bob@gmail.com hello")
    False
    >>> is_email(" bob@gmail.com")
    False
    >>> is_email("bob@gmail.com ")
    True
    >>> is_email("bob@gmail.com  ")
    False
    >>> is_email("bob@gmail.co m")
    True
    >>> is_email("bob@.com")
    False
    >>> is_email("bob.com")
    False
    """
    email_format = re.compile(r'^\w+@[a-zA-Z0-9]+[.].{2,4}$')
    match_object = email_format.search(address)
    return True if match_object else False


def is_nakamoto(name: str) -> bool:
    """
    Determine if the given argument name matches a Nakamoto name format.

    :param name: a string.
    :precondition: provide the function with an argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a bool that represents whether or not the provided string 'name' is a valid Nakamoto name.

    >>> is_nakamoto("Naruto Nakamoto")
    True
    >>> is_nakamoto("NarutoNakamoto")
    False
    >>> is_nakamoto("N Nakamoto")
    True
    >>> is_nakamoto(" Nakamoto")
    False
    >>> is_nakamoto("naruto Nakamoto")
    False
    >>> is_nakamoto("nAruto Nakamoto")
    False
    >>> is_nakamoto("Nakamoto")
    False
    >>> is_nakamoto("Naruto nakamoto")
    False
    >>> is_nakamoto("Naruto Nekamoto")
    False
    >>> is_nakamoto(" Naruto Nakamoto")
    False
    >>> is_nakamoto("Naruto Nakamoto ")
    False
    >>> is_nakamoto("Naruto Nakamoto  ")
    False
    >>> is_nakamoto("Narutonarutonaruto Nakamoto")
    True
    >>> is_nakamoto("Nakamoto Nakamoto")
    True
    >>> is_nakamoto("Naruto Uzumaki Nakamoto")
    False
    """
    nakamoto_name_regex = re.compile('^[A-Z][a-z]* Nakamoto$')
    match_object = nakamoto_name_regex.search(name)
    return True if match_object else False


def is_poker(hand: str) -> bool:
    """
    Determine if the given argument hand represents a valid poker hand.

    In this function 2-9 represents the card ranks 2-9, t represents rank 10, j represents rank jack, q represents
    rank queen, k represents rank king, and a represents rank ace.

    :param hand: a string.
    :precondition: provide the function with a valid argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a bool representing whether the given argument hand is a valid poker hand.

    >>> is_poker("")
    False
    >>> is_poker("a")
    False
    >>> is_poker("aaaa")
    False
    >>> is_poker("aj2376")
    False
    >>> is_poker("a2a898q3kjq")
    False
    >>> is_poker("hello")
    False
    >>> is_poker("226qz")
    False
    >>> is_poker("88888")
    False
    >>> is_poker("59342")
    True
    >>> is_poker("jkqt5")
    True
    >>> is_poker("33taq")
    True
    >>> is_poker("ttkka")
    True
    >>> is_poker("789tj")
    True
    >>> is_poker("88822")
    True
    >>> is_poker("3333a")
    True
    >>> is_poker("tjqka")
    True
    """
    valid_cards_regex = re.compile(r'^[2-9akqjt]{5}$')
    match_object_cards_valid = valid_cards_regex.search(hand)
    if match_object_cards_valid:
        # If there are five valid cards, check if all cards are the same.
        five_of_a_kind_regex = re.compile(r'(\w)\1{4}')
        match_object_five_of_a_kind = five_of_a_kind_regex.search(hand)
        return False if match_object_five_of_a_kind else True
    else:
        return False


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()