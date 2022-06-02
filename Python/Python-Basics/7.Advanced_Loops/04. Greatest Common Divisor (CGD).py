"""
Write a program that finds the CGD - the Greatest Common Divisor of 2 numbers read from the console.
"""


def gcd(a, b):
    while b != 0:
        oldb = b
        b = a % b
        a = oldb
    print('GCD =', a)


def gcd2(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b
    (so that when b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


def main():
    a = int(input())
    b = int(input())
    gcd(a, b)


if __name__ == '__main__':
    main()
