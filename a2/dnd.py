import doctest
import random


def roll_die(number_of_rolls, number_of_sides):
    """
    Simulate rolling dice with a chosen number of sides a chosen number of times.

    :param number_of_rolls: a positive integer representing the number of times the dice should be rolled.
    :param number_of_sides: a positive integer representing the number of sides the dice have.
    :precondition: provide valid arguments to the function as defined by the PARAM statements above.
    :postcondition: return an object as defined by the return statement below.
    :return: a positive integer representing the sum of the dice rolls.

    >>> roll_die(1, 1)
    1
    >>> roll_die(15, 1)
    15
    >>> roll_die(9999, 1)
    9999
    """
    dice_sum = 0
    for i in range(number_of_rolls):
        dice_sum += random.randint(1, number_of_sides)
    return dice_sum


def generate_name(syllables):
    """
    Generate a simple random name of alternating consonants and vowels.

    :param syllables: a positive integer.
    :precondition: provide the function with a valid argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a random string representing a name.
    """
    name = ""
    for i in range(syllables):
        name += generate_syllable()
    return name


def generate_syllable():
    """
    Generate a random syllable composed of a random consonant followed by a random vowel.

    :precondition: provide the function with no arguments.
    :postcondition: return an object as defined by the return statement below.
    :return: a string of length two composed of a consonant followed by a vowel.
    """
    return generate_consonant() + generate_vowel()


def generate_vowel():
    """
    Generate and return a random vowel (including "y").

    :precondition: provide the function with no arguments.
    :postcondition: return an object as defined by the return statement below.
    :return: a string of length one that is a vowel (including "y").
    """
    return random.choice("aeiouy")


def generate_consonant():
    """
    Generate and return a random consonant (including "y").

    :precondition: provide the function with no arguments.
    :postcondition: return an object as defined by the return statement below.
    :return: a string of length one that is a consonant (including "y").
    """
    return random.choice("bcdfghjklmnpqrstvwxyz")


def create_character(syllables):
    """
    Create a properly formatted Dungeons and Dragons character as a dictionary and return it.

    A properly formatted Dungeons and Dragons character is a dictionary object that includes (as values):
    a name (string),
    six statistics (integers in the range [3,18],
    an inventory (a list),
    XP (an integer),
    a class (a string),
    a race (a string), and
    HP (an integer).
    The name, statistics, and HP have random elements in their creation. The inventory and XP are initialized as the
    same value every time. The class and race are chosen from a list of predefined values.

    :param syllables: a positive integer representing the desired syllables in the character name.
    :return: a 
    """
    if not syllables.isdigit() or int(syllables) <= 0:
        print("You have failed to enter a positive integer.")
    else:
        name = generate_name(int(syllables))
        character = {"Name": name,
                     "Strength": roll_die(3, 6),
                     "Intelligence": roll_die(3, 6),
                     "Wisdom": roll_die(3, 6),
                     "Dexterity": roll_die(3, 6),
                     "Constitution": roll_die(3, 6),
                     "Charisma": roll_die(3, 6),
                     "Inventory": [],
                     "XP": 0}
        print("Your character so far is: ")
        print_character(character)
        character["Class"] = select_class()
        character["Race"] = select_race()
        character_health = roll_hit_dice(character["Class"])
        character["HP"] = [character_health, character_health]
        return character


def roll_hit_dice(character_class):
    """
    Generate the starting health for a character based on it's class.

    :param character_class: a string that is a Dungeons and Dragons class in lower case letters.
    :precondition: provide the function with a valid argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: an integer representing the starting health of that character.
    """
    if character_class == "barbarian":
        return roll_die(1, 12)
    elif character_class in ["fighter", "paladin", "ranger"]:
        return roll_die(1, 10)
    elif character_class in ["bard", "cleric", "druid", "monk", "rogue", "warlock"]:
        return roll_die(1, 8)
    else:
        return roll_die(1, 6)


def select_class():
    """
    Ask the user to select a class and then return that class as a string.

    :precondition: TODO
    :postcondition: return an object as defined by the return statement below.
    :return: a string representing the class of the character.
    """
    classes = ["Fighter", "Rogue", "Monk", "Ranger", "Wizard", "Warlock", "Sorcerer", "Cleric", "Druid", "Bard",
               "Barbarian", "Paladin"]
    for i in range(len(classes)):
        print(str(i+1) + " : " + classes[i])

    selection = input("Please pick a class by entering that classes' corresponding integer.")

    while True:
        if selection.isdigit() and int(selection) in range(1, 13):
            break
        selection = input("You have entered an invalid input, please enter an integer in the range [1,12]")

    character_class = classes[int(selection)-1]
    print(character_class)
    return character_class.lower()


def select_race():
    """
    Ask the user to select a race and then return that race as a string.

    :precondition: TODO
    :postcondition: return an object as defined by the return statement below.
    :return: a string representing the race of the character.
    """

    races = ["Tiefling", "Dragonborn", "Human", "Half-Elf", "Elf", "Dwarf", "Gnome", "Halfling", "Half-Orc"]
    for i in range(len(races)):
        print(str(i+1) + " : " + races[i])

    selection = input("Please pick a race by entering that race's corresponding integer.")

    while True:
        if selection.isdigit() and int(selection) in range(1, 10):
            break
        selection = input("You have entered an invalid input, please enter an integer in the range [1,9]")

    character_race = races[int(selection)-1]
    print(character_race)
    return character_race.lower()


def print_character(character):
    """
    Print the provided argument.

    :param character: a printable object.
    :precondition: provide the function with a valid argument as defined by the PARAM statement above.
    :postcondition: print the provided argument.
    """
    print(character)


def choose_inventory(character):
    """
    TODO
    :param character:
    :return:
    """
    shop_message = """    Welcome to the Potion Seller's Store!
    You cannot handle my strongest potions..
    
    So here are some non-potion wares!
    
    1. Ring of Three Wishes
    2. Chris Thompson's Shorts (his favorite beige pair)
    3. Twelve Mostly-Empty Xerox Printer Cartridges
    4. Your Local Politician
    5. Potion Seller's Store
    6. Executive Costco Membership
    7. A Spherical Muffin Where There Is Only Top-Muffin
    8. 0.000176 bitcoin
    9. The Midterm Answers
    10. A Bonus Mark
    
    What would you like to buy?
    (Please enter a list number to buy that item or -1 to leave my store)"""

    items = ["Ring of Three Wishes", "Chris Thompson's Shorts (his favorite beige pair)",
             "Twelve Mostly-Empty Xerox Printer Cartridges",
             "Your Local Politician", "Potion Seller's Store", "Executive Costco Membership",
             "A Spherical Muffin Where There Is Only Top-Muffin",
             "0.000176 bitcoin", "The Midterm Answers", "A Bonus Mark"]
    shopping_basket = []

    purchase = input(shop_message)
    while purchase != "-1":
        if purchase.isdigit() and int(purchase) in list(range(1, 11)):
            shopping_basket.append(items[int(purchase) - 1])
            purchase = input(shop_message)
        else:
            print("Please enter an integer in the range [1,10] or -1.")
            purchase = input(shop_message)
    character["Inventory"].extend(shopping_basket)


def combat_round(opponent_one, opponent_two):
    """

    :param opponent_one: a well-formed dictionary representing a character.
    :param opponent_two: a well-formed dictionary representing a character.
    :return:
    """
    initiative = roll_initiative(opponent_one["Name"], opponent_two["Name"])
    if initiative == opponent_one["Name"]:
        print(opponent_one["Name"] + "'s combat prowess seizes the initiative!")
        roll_to_hit(opponent_one, opponent_two)
        if is_alive(opponent_two):
            roll_to_hit(opponent_two, opponent_one)
            is_alive(opponent_one)
    else:
        print(opponent_two["Name"] + "'s combat prowess seizes the initiative!")
        roll_to_hit(opponent_two, opponent_one)
        if is_alive(opponent_one):
            roll_to_hit(opponent_one, opponent_two)
            is_alive(opponent_two)


def roll_initiative(name_one, name_two):
    initiative_one = roll_die(1, 20)
    print(name_one + " has rolled " + str(initiative_one) + " for initiative!")
    initiative_two = roll_die(1, 20)
    print(name_two + " has rolled " + str(initiative_two) + " for initiative!")
    while initiative_one == initiative_two:
        print("Their agility is a match. " + name_one + " and " + name_two +
              " watch each other intently, waiting for an opening.")
        initiative_one = roll_die(1, 20)
        print(name_one + " has rolled " + str(initiative_one) + " for initiative!")
        initiative_two = roll_die(1, 20)
        print(name_two + " has rolled " + str(initiative_two) + " for initiative!")
    if initiative_one > initiative_two:
        return name_one
    else:
        return name_two


def roll_to_hit(attacker, defender):
    to_hit = roll_die(1, 20)
    print(attacker["Name"] + " has rolled " + str(to_hit) + " to hit against the defender's dexterity of " +
          str(defender["Dexterity"]) + ".")
    if to_hit > defender["Dexterity"]:
        roll_for_damage(attacker, defender)
    else:
        print(attacker["Name"] + " fumbles his strike and misses!")


def roll_for_damage(attacker, defender):
    damage = roll_hit_dice(attacker["Class"])
    defender["HP"][1] -= damage
    print(defender["Name"] + " has been struck for " + str(damage) + " damage.")


def is_alive(character):
    if character["HP"][1] <= 0:
        print(character["Name"] + " has died!")
        alive = False
    else:
        print(character["Name"] + " has " + str(character["HP"][1]) + " HP left!")
        alive = True
    return alive


def main():
    doctest.testmod()
    syllables = input("How many syllables would you like your character to have?")
    player_character = create_character(syllables)
    print_character(player_character)
    choose_inventory(player_character)
    print_character(player_character)
    enemy_character = {"Name": "Solar",
                       "Strength": 26,
                       "Intelligence": 25,
                       "Wisdom": 25,
                       "Dexterity": 14,
                       "Constitution": 26,
                       "Charisma": 30,
                       "Inventory": ["Angelic Weapons", "Divine Awareness", "Innate Spellcasting"],
                       "XP": 33000,
                       "Class": "Paladin",
                       "Race": "human",
                       "HP": [35, 35]}
    combat_round(player_character, enemy_character)


if __name__ == "__main__":
    main()
