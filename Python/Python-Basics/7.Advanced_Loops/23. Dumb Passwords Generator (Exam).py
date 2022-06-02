# 6th March 2016 - SoftUni exam question.
"""
Write a program that reads 2 numbers - n and l and generates alphabetically all possible dumb passwords that  consist of
the following 5 characters:
• Symbol 1: Digit from 1 to n.
• Symbol 2: Digit from 1 through to n.
• Symbol 3: Lowercase letter from the first letters "l" of the Latin alphabet.
• Symbol 4: Lowercase letter from the first letters "l" of the Latin alphabet.
• Symbol 5: Digit from 1 to n, greater than the first 2 symbol-digits.

Input(reading 2 numbers, one per line):
• n - int in the range[1..9]
• l - int in the range[1..9]
Output:
• All "dumb" passwords in alphabetical order, separated by a space.
"""


def solve(n, letter):
    letter = letter + 96                # in order to take the value of the final alphabetical letter

    for symbol_1 in range(1, n):
        for symbol_2 in range(1, n):
            for symbol_3 in range(ord("a"), letter + 1):
                for symbol_4 in range(ord("a"), letter + 1):
                    for symbol_5 in range(1, n + 1):
                        if symbol_5 > symbol_1 and symbol_5 > symbol_2:
                            print(f'{symbol_1}{symbol_2}{chr(symbol_3)}{chr(symbol_4)}{symbol_5}', end=" ")


def main():
    n = int(input())
    letter = int(input())
    solve(n, letter)


if __name__ == '__main__':
    main()
