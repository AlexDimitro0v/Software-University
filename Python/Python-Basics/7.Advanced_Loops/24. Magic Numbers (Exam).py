# 26th March 2016 - SoftUni exam question.
"""
Write a program that reads a magic number and outputs all possible 6-digit numbers, whose product of its numbers is
equal to the magic number.
Example:
Magic Number: 2
• 111112 -> 1 * 1 * 1 * 1 * 1 * 2 = 2
• 111121 -> 1 * 1 * 1 * 1 * 2 * 1 = 2
• 111211 -> 1 * 1 * 1 * 2 * 1 * 1 = 2
• 112111 -> 1 * 1 * 2 * 1 * 1 * 1 = 2
• 121111 -> 1 * 2 * 1 * 1 * 1 * 1 = 2
• 211111 -> 2 * 1 * 1 * 1 * 1 * 1 = 2

Input:
• A single magic number
Output:
• All the numbers whose product is equal to the magic number, separated by a space.
"""


def solve(magic_number):
    for digit1 in range(1, 10):
        if digit1 > magic_number:
            break
        for digit2 in range(1, 10):
            if digit2 > magic_number:
                break
            for digit3 in range(1, 10):
                if digit3 > magic_number:
                    break
                for digit4 in range(1, 10):
                    if digit4 > magic_number:
                        break
                    for digit5 in range(1, 10):
                        if digit5 > magic_number:
                            break
                        for digit6 in range(1, 10):
                            if digit1 * digit2 * digit3 * digit4 * digit5 * digit6 > magic_number:
                                break
                            elif digit1 * digit2 * digit3 * digit4 * digit5 * digit6 == magic_number:
                                print(f'{digit1}{digit2}{digit3}{digit4}{digit5}{digit6}', end=" ")


def solve2(magic_number):
    # another way - slow, but easy to debug

    c = []
    h = []
    for i in range(1, 10):
        if magic_number < i:
            break
        if magic_number % i == 0:   # takes the numbers up to n
            c.append(i)             # adds them to a list

    for a in c:
        for b in c:
            for d in c:
                for e in c:
                    for f in c:
                        for g in c:
                            mn = int(str(a) + str(b) + str(d) + str(e) + str(f) + str(g))  # all 6-digit number strings
                            h.append(mn)  # adding them to a list

    for k in h:
        s = 1

        for j in str(k):
            s = s * int(j)  # multiplying all the 6 digits

        if s == magic_number:
            print(k, end=' ')


def main():
    magic_number = int(input())
    solve(magic_number)


if __name__ == '__main__':
    main()
