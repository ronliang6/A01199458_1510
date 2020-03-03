import doctest
import itertools


def create_board() -> list:
    return list(itertools.product([i for i in range(5)], repeat=2))





def main():
    doctest.testmod()
    game()


if __name__ == "__main__":
    main()
