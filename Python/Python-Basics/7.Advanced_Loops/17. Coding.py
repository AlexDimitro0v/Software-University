"""
Write a program that reads an integer number with N digits and outputs N lines with symbols on it. Start with the
ones, then tens, hundreds and so on...
The symbols must satisfy the following conditions:
• The symbol is to be found in the ASCII table. It's decimal ASCII code is found by adding 33 to the current digit
corresponding to that line
• The symbol is printed as many times as the digit corresponding to that line.
• If for a given line you have a digit 0, print 'ZERO' and nothing else.

Example:
Input:
2049

Output:
*********
%%%%
ZERO
##
"""


def solve(n):
    for digit in n[::-1]:               # or in reversed(n)
        for times in range(int(digit)):
            print(chr(int(digit)+33), end='')
        if digit == '0':
            print('ZERO', end='')
        print()


def main():
    n = input()
    solve(n)


if __name__ == '__main__':
    main()

