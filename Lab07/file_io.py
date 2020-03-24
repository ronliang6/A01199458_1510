import doctest


def find_common_words():
    """
    Print a list of the ten most common words in a text file and their number of occurrences.

    Basic text-cleaning has been done. Many symbols have been removed but there are a few notable errors. Contracted
    words will not parse properly as the "'" symbol is replaced with a space. Additionally, words continue to the
    next line with the use of a hyphen also do not read correctly. Numbers and non-word "strings" also count as
    words. Hypothetically, a number could be the most common "word" in a text file.

    :precondition: provide a possibly non-existent text file as a directory to the first input prompt.
    :postcondition: print the ten most common words and their occurrences. If there are less than ten unique words,
    print those words and their occurrences.
    :raise FileNotFoundError: if the file cannot be found.
    """
    file_name = input("What is the name of the file you wish to operate on?")
    try:
        with open(file_name) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print("The file cannot be found.")
    else:
        word_tally = {}
        for line in lines:
            cleaned_line = string_cleaner(line)
            for word in cleaned_line.split():
                word = word.lower()
                if word in word_tally.keys():
                    word_tally[word] += 1
                else:
                    word_tally[word] = 1
        for word, occurrences in sorted(word_tally.items(), key=get_second_object, reverse=True)[:10]:
            print(word, "-", occurrences)


def string_cleaner(string: str) -> str:
    """
    Replace certain symbols in a string with white spaces.

    :param string: a string.
    :precondition: provide the function with a valid argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a string with certain symbols replaced with white spaces.

    >>> string_cleaner("")
    ''
    >>> string_cleaner(",")
    ' '
    >>> string_cleaner(".,()/")
    '     '
    >>> string_cleaner('1')
    '1'
    >>> string_cleaner('2r5 3z,. 1(')
    '2r5 3z   1 '
    >>> string_cleaner("hello how are you")
    'hello how are you'
    """
    symbols_to_remove = [",", ".", "(", ")", '"', "!", "&", "-", "~", "/", "'"]
    for symbol in symbols_to_remove:
        string = string.replace(symbol, " ")
    return string


def get_second_object(iterable):
    return iterable[1]


def main():
    doctest.testmod()
    find_common_words()


if __name__ == "__main__":
    main()
