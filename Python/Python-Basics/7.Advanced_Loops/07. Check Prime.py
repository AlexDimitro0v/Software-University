"""
Write a program to check if a number is prime or not - i.e if the number divides only be itself and 1 and is greater
than 1.
"""
# A prime number can divide only by itself and 1(without remainder). => 9 is not a prime since it divides by 1, 3 nad 9.
import math


def check_prime(n):                         # naive way
    if n == 2:
        number = "Prime"
    elif n < 2 or n == 3:
        number = "Not Prime"
    else:
        quadrant = math.sqrt(n)             # returns the square root: 16->4
        for i in range(2, int(quadrant + 1)):
            divide = n / i
            if divide.is_integer():         # checking if the numbers divides by any other number
                number = "Not Prime"
                break
            else:
                number = "Prime"
    return number


# another way - for loop
def prime_or_not(n):
    prime = True

    if n < 2:
        prime = False
    else:
        square_root = int(math.sqrt(n))
        for i in range(2, square_root+1):
            if n % i == 0:
                prime = False
                break
    return prime


# another way - while loop
def prime_number(n):
    prime = True
    if n < 2:
        print("Not Prime")
        return
    square_root = int(math.sqrt(n))
    i = 2
    while i <= square_root:
        if n % i == 0:
            prime = False
            break
        i += 1

    # Print if prime is found
    if prime:
        print("Prime")
    else:
        print("Not Prime")


def main():
    n = int(input())
    prime_number(n)


if __name__ == '__main__':
    main()
