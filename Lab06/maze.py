import doctest
import itertools


def create_board() -> list:
    return list(itertools.product([i for i in range(5)], repeat=2))


def create_character() -> list:
    return [0, 0]


def display_position(game_board: list, character: list):
    print("You are currently here:")
    for position in game_board:
        if position[0] == character[0] and position[1] == character[1]:
            print('C', end=" ")
        else:
            print("*", end=" ")
        if position[1] == 4:
            print("")


def validate_move(board: list, character: list, direction: str) -> bool:
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
    if direction == "d":
        character[1] += 1
    if direction == "a":
        character[1] -= 1
    if direction == "w":
        character[0] -= 1
    if direction == "s":
        character[0] += 1


def is_win(character: list) -> bool:
    if character[0] == 4 and character[1] == 4:
        return True
    else:
        return False





def main():
    doctest.testmod()
    game()


if __name__ == "__main__":
    main()
