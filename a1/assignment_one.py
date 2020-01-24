def convert_to_roman_numeral(positive_int):
    ones_list = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens_list = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds_list = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

    length = len(str(positive_int))
    roman_numeral = ones_list[int(str(positive_int)[-1])]

    if length > 1:
        roman_numeral = tens_list[int(str(positive_int)[-2])] + roman_numeral

    if length > 2:
        roman_numeral = hundreds_list[int(str(positive_int)[-3])] + roman_numeral

    if length > 3:
        roman_numeral = "M" * int(str(positive_int)[-4]) + roman_numeral

    if length > 4:
        roman_numeral = 10 * "M" + roman_numeral

    return roman_numeral


def main():
    print(convert_to_roman_numeral(7386))


if __name__ == "__main__":
    main()
