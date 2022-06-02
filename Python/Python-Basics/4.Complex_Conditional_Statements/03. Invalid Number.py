"""
A given number is valid if it is in the range [100-200] or 0. Write a program that outputs "invalid" if the number
is not a valid one.
"""


def is_valid(number):
    if number == 0 or number in range(100, 201):        # 200 inclusive
        number = "valid"                # just for the sake of the demo
        pass                            # pass is a common practice in Python
    else:
        print("invalid")


def check_validity(number):                             # just another solution option
    if not number == 0 or number in range(100, 201):
        print("invalid")


def main():
    number = int(input("Enter a number: "))
    is_valid(number)


if __name__ == '__main__':
    main()
