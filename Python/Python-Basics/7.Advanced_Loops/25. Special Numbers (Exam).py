# 24th April 2016 - SoftUni exam question.
"""
Write a program that reads an integer(N) and outputs all possible "special" numbers between 1111 and 9999.
In order a number to be a special one, N must to be divisible by all of his digits without remainder.
Example:
N = 16  => Special Numbers = 2418
• 16/2 = 8  without remainder
• 16/4 = 4  without remainder
• 16/1 = 16 without remainder
• 16/8 = 2  without remainder

Input:
• A single integer number - N
Output:
• All the special numbers, separated by a space.
"""


def solve(n):
    for digit1 in range(1, 10):
        if digit1 > n:
            break
        elif n % digit1 == 0:
            for digit2 in range(1, 10):
                if digit2 > n:
                    break
                elif n % digit2 == 0:
                    for digit3 in range(1, 10):
                        if digit3 > n:
                            break
                        elif n % digit3 == 0:
                            for digit4 in range(1, 10):
                                if digit4 > n:
                                    break
                                elif n % digit4 == 0:
                                    print(f'{digit1}{digit2}{digit3}{digit4}', end=" ")


def main():
    n = int(input())
    solve(n)


if __name__ == '__main__':
    main()
