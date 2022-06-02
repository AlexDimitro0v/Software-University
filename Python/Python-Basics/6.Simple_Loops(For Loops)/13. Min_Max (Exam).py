"""
Write a program that reads n number of integers (n>0) entered by the user and finds the smallest as well as the
biggest among them.

Input:
• First Line - n (the number of integers to be entered from the user).
• The next n lines - a single integer per line.
Output:
• The smallest number
• The biggest number

Note: Solve the task by using a list data structure.
"""


def solve(n):
    numbers_list = []
    for num in range(n):
        number = int(input())
        numbers_list.append(number)

    try:
        max_number = max(numbers_list)
        min_number = min(numbers_list)
    except ValueError:
        min_number, max_number = 0, 0

    print(f"Max number: {max_number}")
    print(f"Min number: {min_number}")


def help_function():
    print(help(min))
    print(help(max))


def main():
    solve(int(input()))


if __name__ == '__main__':
    main()
