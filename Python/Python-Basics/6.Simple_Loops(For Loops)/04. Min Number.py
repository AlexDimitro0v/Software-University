"""
Write a program that reads n number of integers (n>0) entered by the user and finds the smallest among them.

Input:
• First Line - n (the number of integers to be entered from the user).
• The next n lines - a single integer per line.
Output:
• The smallest number
Example:
    Input               Output
       3
      20
      -4
      10                  -4

Note: Solve the task by using a list data structure.
"""


def find_min(n):
    numbers_list = []
    for num in range(n):
        number = int(input())
        numbers_list.append(number)

    try:
        min_number = min(numbers_list)
    except ValueError:
        return "No numbers provided."
    return min_number


def main():
    print("n = ", end="")
    print("min =", find_min(int(input())))


def min_description():
    print(help(min))


if __name__ == '__main__':
    main()
