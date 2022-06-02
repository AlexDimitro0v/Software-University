"""
Write a program that reads and outputs an even number. If the entered number is not even, the user is prompted to enter
a new number until the number is even.
"""


def solve(n):
    while True:
        if n % 2 == 0:
            print("Even number entered:", n)
            break
        print("Invalid number!")
        n = int(input("Enter even number: "))


# another way
def solve2(n):
    while not n % 2 == 0:
        print("Invalid number!")
        n = int(input("Enter even number: "))

    print("Even number entered:", n)


# another way
def solve3():
    while True:
        n = int(input("Enter even number: "))
        if n % 2 == 0:
            break
        print("The number is not even.")

    print("Even number entered: " + str(n))


def main():
    n = int(input("Enter even number: "))
    solve2(n)


if __name__ == '__main__':
    main()
