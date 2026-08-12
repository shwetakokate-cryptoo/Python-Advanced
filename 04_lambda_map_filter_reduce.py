from functools import reduce


def main():

    numbers = [1, 2, 3, 4, 5, 6]

    square = lambda number: number ** 2
    squares = list(map(square, numbers))

    even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

    total = reduce(lambda first, second: first + second, numbers)

    print("Original Numbers:")
    print(numbers)

    print("\nSquares:")
    print(squares)

    print("\nEven Numbers:")
    print(even_numbers)

    print("\nSum of Numbers:")
    print(total)


if __name__ == "__main__":
    main()
