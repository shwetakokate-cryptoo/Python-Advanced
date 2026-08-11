"""
Python Iterators

This program demonstrates the iterator protocol
using __iter__() and __next__().
"""


class NumberIterator:

    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.end:
            raise StopIteration

        number = self.current
        self.current += 1

        return number


def main():

    numbers = NumberIterator(1, 5)

    print("Iterator Values:")

    for number in numbers:
        print(number)


if __name__ == "__main__":
    main()
