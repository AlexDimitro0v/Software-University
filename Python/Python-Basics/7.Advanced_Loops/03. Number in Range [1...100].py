"""
Write a program that reads and outputs a number in the range[1..100]. If the entered number is outside the range,
the user is prompted to enter a new number until the number lies in the range.
"""


def solve1(number):
    while number < 1 or number > 100:  # while is in the right range
        print("Invalid number!")
        number = int(input("Give me a number: "))

    print("The number is: {}".format(number))


def solve2(n):
    while True:
        if n in range(1, 101):
            print("The number is: {}".format(n))
            break
        else:
            print("Invalid number!")
            n = int(input())


def solve3(number):
    while not 1 <= number <= 100:  # while it's not in the right range
        print("Invalid number!")
        number = int(input())

    print("The number is: {}".format(number))


def main():
    number = int(input())
    solve3(number)


if __name__ == '__main__':
    main()
