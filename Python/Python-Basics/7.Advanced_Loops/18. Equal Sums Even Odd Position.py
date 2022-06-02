"""
Write a program that reads 2 integer numbers - the second one always being greater than the first one and prints all the
number in between them that have a sum of the numbers at even positions equal to the sum of the numbers at odd positions.
"""


def solve(n1, n2):
    for number in range(n1, n2+1):
        odd_sum = sum(map(int, str(number)[::2]))      # taking the odd sum via casting and list slicing
        even_sum = sum(map(int, str(number)[1::2]))    # taking the even sum via casting and list slicing
        if odd_sum == even_sum:
            print(number, end=' ')


def main():
    n1 = int(input())
    n2 = int(input())
    solve(n1, n2)


if __name__ == '__main__':
    main()
