import doctest


def print_food_summary(food_information: dict):
    """
    Print a sorted number of foods given as keys in a dictionary.

    :param food_information: a dictionary with strings that represent food items as keys.
    :precondition: provide this function with an argument as defined by the PARAM statement above.
    :postcondition: print an alphabetically sorted and formatted list of food items.

    >>> print_food_summary({"ham": 50, "cheese": 20, "carrots": 10})
    <BLANKLINE>
    Food Items: ['carrots', 'cheese', 'ham']
    >>> print_food_summary({"ham": 50})
    <BLANKLINE>
    Food Items: ['ham']
    >>> print_food_summary({})
    <BLANKLINE>
    Food Items: []
    """
    food_item_names = []
    for item in food_information:
        food_item_names.append(item)
    print("\nFood Items:", sorted(food_item_names))


def print_calorie_summary(food_information: dict):
    """
    Print statistical information about food calories.

    :param food_information: a non-zero length dictionary of food items as keys (strings) and their respective
    calories as values (integers).
    :precondition: provide the function with an argument as defined by the PARAM statement above.
    :postcondition: print out the mean calorie of all food items as well as the total.

    >>> print_calorie_summary({"ham": 50, "cheese": 20, "carrots": 10})
    Total Calories: 80 Average Calories: 26.7
    <BLANKLINE>
    >>> print_calorie_summary({"ham": 50})
    Total Calories: 50 Average Calories: 50.0
    <BLANKLINE>
    >>> print_calorie_summary({"ham": 0})
    Total Calories: 0 Average Calories: 0.0
    <BLANKLINE>
    """
    total_calories = 0
    for item in food_information:
        total_calories += food_information[item]

    avg_calories = total_calories / len(food_information)

    print("Total Calories:", total_calories,
          "Average Calories: %0.1f\n" % avg_calories)


def main():
    """
    Add any number of user-prompted foods with calorie information to a initialized dictionary and print summary
    information every time a new item is added.

    The information summary is an alphabetically sorted list of foods and the calorie total as well as the mean.

    :precondition: do not provide items that already exist, including in the initialized dictionary of foods. Do not
    provide non-integer entries for calorie information.
    :postcondition: add foods to a dictionary and print summary information about all existing foods.
    """
    doctest.testmod()
    calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
                "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
                "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102
                }
    new_item = input("Enter food item to add, or 'q' to exit: ")
    while new_item != "q":
        new_item_calories = int(input("Enter calories for " + new_item + ": "))
        calories[new_item] = new_item_calories
        print_food_summary(calories)
        print_calorie_summary(calories)
        new_item = input("Enter food item to add, or 'q' to exit: ")


if __name__ == "__main__":
    main()
