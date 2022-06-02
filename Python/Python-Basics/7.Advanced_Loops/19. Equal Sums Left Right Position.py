"""
Write a program that reads 2 5-digit-integer numbers - the second one always being greater than the first one and prints
all the numbers in between them, separated by a space, that satisfy the following conditions:
• The sum of the 2 rightmost and the 2 leftmost digits of the checked number are equal.
• Or If the mentioned sums are not equal, add the middle digit to the smaller sum and check if the resulting new sum is
equal to the other sum.
    o If the sums are equal, print the number
    o Otherwise continue searching
"""


def solve(n1, n2):
    for number in range(n1, n2+1):
        a = sum(map(int, str(number)[:2]))      # sum of the first 2 numbers
        b = sum(map(int, str(number)[-2:]))     # sum of the last 2 numbers
        if a == b:
            print(number, end=' ')
        else:
            if a > b:
                b += int(str(number)[2])
                if a == b:
                    print(number, end=' ')
            else:
                a += int(str(number)[2])
                if a == b:
                    print(number, end=' ')


def main():
    n1 = int(input())
    n2 = int(input())
    solve(n1, n2)


if __name__ == '__main__':
    main()
