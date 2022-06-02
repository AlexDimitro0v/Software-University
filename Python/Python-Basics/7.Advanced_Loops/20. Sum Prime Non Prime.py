"""
Write a program that repeatedly reads integer numbers until the command 'stop' is entered and finds the sum of all prime
and non-prime numbers. Since by definition from the maths the negative numbers cannot be primes, if a negative number
is entered in the console, simply print 'Number is negative' and ignore the number without adding it to either sums and
wait for the next number to be entered.
Output:
• "Sum of all prime numbers is: {prime numbers sum}"
• "Sum of all non prime numbers is: {non-prime numbers sum}"
"""


import math


def is_prime(n):
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


def solve():
    number = input()
    prime_numbers_sum = 0
    non_prime_numbers_sum = 0
    while number != 'stop':
        if is_prime(int(number)):
            prime_numbers_sum += int(number)
        elif int(number) < 0:                   # avoid negative numbers
            print("Number is negative.")
        else:
            non_prime_numbers_sum += int(number)
        number = input()

    print(f"Sum of all prime numbers is: {prime_numbers_sum}")
    print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")


if __name__ == '__main__':
    solve()
