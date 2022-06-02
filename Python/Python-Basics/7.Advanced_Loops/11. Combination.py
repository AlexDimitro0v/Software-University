"""
Write a program that calculates how many natural numbers (including 0) are there in the following equation:
x1+x2+x3+x4+x5 = n where n will be entered from the console.
"""


def combinations(n):
    counter = 0
    for digit1 in range(n+1):
        for digit2 in range(n+1):
            for digit3 in range(n+1):
                for digit4 in range(n+1):
                    for digit5 in range(n+1):
                        if digit1+digit2+digit3+digit4+digit5 == n:
                            counter += 1
    return counter


def main():
    n = int(input())
    print(combinations(n))


if __name__ == '__main__':
    main()


