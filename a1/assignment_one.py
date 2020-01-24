def digit_converter(positive_int, length):
    ones_list = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens_list = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds_list = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

    if length == "ones":
        return ones_list[int(str(positive_int)[-1])]
    if length == "tens":
        return tens_list[int(str(positive_int)[-2])]
    if length == "hundreds":
        return hundreds_list[int(str(positive_int)[-3])]
    if length == "thousands":
        return "M" * int(str(positive_int)[-4])
    if length == "ten thousands":
        return "M" * 10


def convert_to_roman_numeral(positive_int):
    length = len(str(positive_int))

    roman_numeral = digit_converter(positive_int, "ones")
    if length > 1:
        roman_numeral = digit_converter(positive_int, "tens") + roman_numeral
    if length > 2:
        roman_numeral = digit_converter(positive_int, "hundreds") + roman_numeral
    if length > 3:
        roman_numeral = digit_converter(positive_int, "thousands") + roman_numeral
    if length > 4:
        roman_numeral = digit_converter(positive_int, "ten thousands") + roman_numeral

    return roman_numeral


def main():
    print(convert_to_roman_numeral(1999))


if __name__ == "__main__":
    main()
