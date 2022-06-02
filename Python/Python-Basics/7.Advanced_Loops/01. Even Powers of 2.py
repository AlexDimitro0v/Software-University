# Write a program prints the numbers from 1 to 2^n(2 to the power of n), but only the even powers.
# Example: 2^0  2^2  2^4 2^6 ... 2^n


def solve(n):
    for i in range(0, n+1, 2):
        print(pow(2, i))


def solve2(n):
    num = 1
    for i in range(0, n+1, 2):
        print(num)
        num = num * 4


def main():
    n = int(input())
    solve(n)


if __name__ == '__main__':
    main()
