def convert_to_roman_numeral(positive_int):
    length = len(str(positive_int))
    roman_numeral = ""
    for i in range(length):
        roman_numeral = digit_converter(positive_int, length, i) + roman_numeral
    return roman_numeral


def digit_converter(positive_int, length, i):
    roman_numeral_list = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                          ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                          ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                          ["", "M", "MM", "MMM", "MMMM", "MMMMM", "MMMMMM", "MMMMMMM", "MMMMMMMM", "MMMMMMMMM"],
                          ["", "MMMMMMMMMM"]]

    return roman_numeral_list[i][int(str(positive_int)[-(i+1)])]


def colour_mixer():
    first_colour = input("please enter a primary colour (red, yellow, or blue)")
    second_colour = input("please enter a different primary colour")
    if (first_colour == "red" or first_colour == "blue" or first_colour == "yellow") and \
            (second_colour == "red" or second_colour == "blue" or second_colour == "yellow"):
        if first_colour == second_colour:
            print("You have entered the same colour twice. "
                  "Please enter two different primary colours (red, yellow, or blue).")
        elif first_colour == "red":
            if second_colour == "yellow":
                print("orange")
            elif second_colour == "blue":
                print("purple")
        elif first_colour == "yellow":
            if second_colour == "red":
                print("orange")
            elif second_colour == "blue":
                print("green")
        elif first_colour == "blue":
            if second_colour == "yellow":
                print("green")
            elif second_colour == "red":
                print("purple")
    else:
        print("You have entered at least one invalid colour. "
              "Please enter a primary colour (red, yellow, or blue) twice.")


def main():
    print(convert_to_roman_numeral(3313))
    colour_mixer()


if __name__ == "__main__":
    main()
