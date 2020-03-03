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




def main():
    doctest.testmod()
    game()


if __name__ == "__main__":
    main()
