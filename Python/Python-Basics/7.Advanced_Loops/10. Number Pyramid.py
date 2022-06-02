"""
Write a program that reads a n(number) and prints a pyramid of numbers up to n(including).
"""


def pyramid_of_numbers(n):
    num = 1
    for row in range(1, n+1):       # 7
        for col in range(row):      # 49
            print(num, end=' ')
            num += 1
            if num > n:
                break
        print()
        if num > n:
            break


def main():
    n = int(input())
    pyramid_of_numbers(n)


if __name__ == '__main__':
    main()
