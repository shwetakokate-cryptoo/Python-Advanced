"""
Python Generators

This program demonstrates generators
using the yield keyword.
"""


def number_generator(start: int, end: int):
    for number in range(start, end + 1):
        yield number


def square_generator(numbers):
    for number in numbers:
        yield number ** 2


def main():

    numbers = number_generator(1, 5)

    print("Generated Numbers:")

    for number in numbers:
        print(number)

    print("\nGenerated Squares:")

    squares = square_generator(number_generator(1, 5))

    for square in squares:
        print(square)


if __name__ == "__main__":
    main()
