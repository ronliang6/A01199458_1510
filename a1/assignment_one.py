def convert_to_roman_numeral(positive_int):
    length = len(str(positive_int))
    roman_numeral = ""
    roman_numeral_list = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                          ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                          ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                          ["", "M", "MM", "MMM", "MMMM", "MMMMM", "MMMMMM", "MMMMMMM", "MMMMMMMM", "MMMMMMMMM"],
                          ["", "MMMMMMMMMM",]]

    for i in range(length):
        roman_numeral = roman_numeral_list[i][int(str(positive_int)[-(i+1)])] + roman_numeral
    return roman_numeral


def main():
    print(convert_to_roman_numeral(3313))


if __name__ == "__main__":
    main()
