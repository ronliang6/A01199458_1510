import doctest
import itertools


def create_board() -> list:
    """
    Create a two-dimensional game board with a 5 by 5 grid represented by a list of tuples.

    :precondition: provide the function with no arguments.
    :postcondition: return an object as defined by the return statement below.
    :return: a list of tuples representing a game board.
    """
    return list(itertools.product([i for i in range(5)], repeat=2))


def create_character() -> list:
    """
    Return a list with two zeroes.

    :precondition: provide the function with no arguments.
    :postcondition: return an object as defined by the return statement below.
    :return: a list of two zeroes that represent the starting position of a character.
    """
    return [0, 0]


def display_position(game_board: list, character: list):
    """
    Print a visual representation of where the character is on the game board.

    :param game_board: a non-zero list of tuples representing the game board.
    :param character: a list of two integers representing a valid position on the board.
    :precondition: provide the function with valid arguments according to the PARAM statements above.
    :postcondition: print a visual representation of the board and where the character is on that board.
    """
    print("You are currently here:")
    for position in game_board:
        if position[0] == character[0] and position[1] == character[1]:
            print('C', end=" ")
        else:
            print("*", end=" ")
        if position[1] == 4:
            print("")


def validate_move(board: list, character: list, direction: str) -> bool:
    """
    Determine if a given direction is valid for a character to move while on a game board.

    :param board: a non-zero list of tuples representing the game board.
    :param character: a list of two integers representing a character's position.
    :param direction: a string representing directional movement as a 'wasd' letter.
    :precondition: provide the function with valid arguments according to the PARAM statements above.
    :postcondition: return an object as defined by the return statement below.
    :return: a bool representing whether or not a given direction is a valid.

    >>> validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], [0, 0], "d")
    True
    >>> validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], [1, 1], "s")
    False
    >>> validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], [1, 0], "w")
    True
    >>> validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], [0, 1], "a")
    True
    """
    max_x_y_coordinates = board[-1]
    valid_options = []
    if character[1] < max_x_y_coordinates[0]:
        valid_options.append("d")
    if character[1] > 0:
        valid_options.append("a")
    if character[0] < max_x_y_coordinates[1]:
        valid_options.append("s")
    if character[0] > 0:
        valid_options.append("w")
    if direction in valid_options:
        return True
    else:
        return False


def move_character(direction: str, character: list):
    """
    Update a character's position given a direction and that character's current position.

    :param direction: a string that is a 'wasd' letter representing a direction.
    :param character: a list of two integers representing a character's position.
    :precondition: provide the function with valid arguments according to the PARAM statements above.
    :postcondition: update the character's position.
    """
    if direction == "d":
        character[1] += 1
    if direction == "a":
        character[1] -= 1
    if direction == "w":
        character[0] -= 1
    if direction == "s":
        character[0] += 1


def is_win(character: list) -> bool:
    """
    Determine if a character is at the end of a maze based on that character's position.

    :param character: a list of two integers representing a character position.
    :precondition: provide the function with a valid argument according to the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a bool representing whether or not the character is at the end of a maze.

    >>> is_win([1, 4])
    False
    >>> is_win([4, 4])
    True
    >>> is_win([0, 0])
    False
    """
    if character[0] == 4 and character[1] == 4:
        return True
    else:
        return False


def game():
    """
    Simulate a simple maze game for the user.

    The game is played on a grid of 5 by 5 positions. The user can move to adjacent but not diagonally. The user
    starts at position 0, 0. The character can be moved by inputting a wasd key.
    :precondition: the function is provided with no arguments.
    :postcondition: the user plays a maze game and will probably eventually win.
    """
    board = create_board()
    character = create_character()
    reached_goal = False
    while not reached_goal:
        display_position(board, character)
        direction = input("Please enter a key in 'wasd' to move that direction. You cannot move pass the edge of the "
                          "map.")
        if validate_move(board, character, direction):
            move_character(direction, character)
            reached_goal = is_win(character)
        else:
            print("Please select a valid input. Enter a wasd key and do not move past the walls!")
    display_position(board, character)
    print("You win!")


def main():
    """
    Run the functions in this module and doctest them.
    """
    doctest.testmod()
    game()


if __name__ == "__main__":
    main()
