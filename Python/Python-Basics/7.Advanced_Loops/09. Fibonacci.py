"""
Write a program that reads n(number) from the console and finds the nth number of the fibonacci sequence,
assuming we start from 0.
0 -> 1
1 -> 1
2 -> 2
3 -> 3
4 -> 5
5 -> 8
"""


def find_fib_number(n):
    f0 = 1
    f1 = 1
    for i in range(n-1):
        f_next = f0 + f1
        f0 = f1
        f1 = f_next

    print(f1)


# smarter way
def fib(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, a + b
    print(b)


def main():
    n = int(input())
    fib(n)


if __name__ == '__main__':
    main()
