"""
Python Decorators

This program demonstrates how decorators
can extend the behavior of functions.
"""


def logger(function):

    def wrapper():

        print("Function execution started.")

        function()

        print("Function execution completed.")

    return wrapper


@logger
def greet():

    print("Welcome to Python Advanced.")


def main():

    greet()


if __name__ == "__main__":
    main()
