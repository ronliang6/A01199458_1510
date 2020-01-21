"""
Create a variety of errors.
"""


def main():
    """Generate a ZeroDivisionError, two IndexErrors, and two TypeErrors."""

    print(1 / 0)

    error_list = ["one", "two", "three"]
    print(error_list[len(error_list)])
    print(error_list[-4])

    print("Hello, I am " + 21)
    weeks_in_year = 365 / "7"


if __name__ == "__main__":
    main()
