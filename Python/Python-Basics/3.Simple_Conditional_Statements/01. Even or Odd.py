"""
Write a console program that reads a number from the console and prints even or odd in response to that number.
Note: The number should be an integer.
"""


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def is_odd(number):
    if number % 2 == 1:
        return True
    return False


if __name__ == '__main__':
    number_input = int(input("Give me a whole number: "))
    if is_even(number_input):
        print("even")
    elif is_odd(number_input):
        print("odd")
    else:
        print("This is not a whole number.")
