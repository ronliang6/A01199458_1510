

def find_common_words():
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
        words_printed = 0
        for word, occurrences in sorted(word_tally.items(), key=sort_by_value, reverse=True):
            if words_printed == 10:
                break
            print(word, "-", occurrences)


def string_cleaner(string):
    symbols_to_remove = [",", ".", "(", ")", '"', "!", "&", "-", "~", "/"]
    for symbol in symbols_to_remove:
        string = string.replace(symbol, " ")
    return string


def sort_by_value(item):
    return item[1]
