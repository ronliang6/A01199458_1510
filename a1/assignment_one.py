import random


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


def time_converter(seconds, days, hours, minutes):
    if seconds >= 86400:
        return time_converter(seconds - 86400, days + 1, hours, minutes)
    elif seconds >= 3600:
        return time_converter(seconds - 3600, days, hours + 1, minutes)
    elif seconds >= 60:
        return time_converter(seconds - 60, days, hours, minutes + 1)
    else:
        print(str(days) + " " + str(hours) + " " + str(minutes) + " " + str(seconds))


def time_calculator(seconds):
    time_converter(seconds, 0, 0, 0)


def compound_interest(principal, annual_interest, compound_frequency, time_years):
    new_balance = principal * pow((1 + annual_interest/compound_frequency), (compound_frequency * time_years))
    return new_balance


def rock_paper_scissors():
    raw_input = input('Please enter "rock", "paper", or "scissors" to play this game.')
    player_choice = raw_input.strip().lower()
    if player_choice != "rock" and player_choice != "paper" and player_choice != "scissor":
        print('You have entered an invalid choice. The acceptable choices are "rock", "paper", or "scissors".')
    else:
        outcome = "don't win."
        random_number = random.randint(0, 2)
        if random_number == 0:
            computer_choice = "rock"
            if player_choice == "paper":
                outcome = "win."
        elif random_number == 1:
            computer_choice = "paper"
            if player_choice == "scissors":
                outcome = "win."
        else:
            computer_choice = "scissors"
            if player_choice == "rock":
                outcome = "win."
        print("The computer picked " + computer_choice + ". You picked " + player_choice + ". You " + outcome)


def number_generator():
    return number_generator_helper([])


def number_generator_helper(numbers_list):
    new_number = random.randint(1, 49)
    if len(numbers_list) <= 5:
        if new_number in numbers_list:
            return number_generator_helper(numbers_list)
        else:
            numbers_list.append(new_number)
            return number_generator_helper(numbers_list)
    else:
        numbers_list.sort()
        return numbers_list


def main():
    print(convert_to_roman_numeral(3313))
    colour_mixer()
    time_calculator(94553)
    print(compound_interest(100, 0.02, 2, 10))
    rock_paper_scissors()
    print(number_generator())


if __name__ == "__main__":
    main()
