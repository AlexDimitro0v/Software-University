"""
Print all numbers from 1 to n with a step *2+1.
"""


def solve1(n):
    num = 1
    for i in range(1, n+1):
        print(num)
        num = num * 2 + 1
        if num > n:
            break


def solve2(n):
    # while loop solution
    num = 1
    while num <= n:
        print(num)
        num = num * 2 + 1  # increment, so the while loop is not infinitive


def main():
    n = int(input())
    solve2(n)


if __name__ == '__main__':
    main()
