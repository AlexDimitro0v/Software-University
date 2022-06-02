# 26th March 2016 - SoftUni exam question.
"""
There are n integers in the range[0..100]. Depending on the range, some of these are:
• divide by 2 without remainder - p1% from the whole
• divide by 3 without remainder - p2% from the whole
• divide by 4 without remainder - p3% from the whole

Write a program that calculates and outputs the p1,p2 and p3 percents.

Input:
• First Line - n (the number of integers to be entered from the user).
• The next n lines - a single integer per line.
Output:
• 3 Lines, containing a number between 0% and 100% - p1,p2,p3.

Note: Format the percents with 2 places after the decimal point.
"""


def solve(n):
    p1 = 0
    p2 = 0
    p3 = 0

    for i in range(1, n+1):
        number = int(input())

        if number % 2 == 0:
            p1 += 1
        if number % 3 == 0:
            p2 += 1
        if number % 4 == 0:
            p3 += 1
        my_list = [p1, p2, p3]
        my_list = [elem / n * 100 for elem in my_list]              # elegant way with list comprehension
        my_formatted_list = ['%.2f' % elem for elem in my_list]

    for element in my_formatted_list:
        print(str(element) + "%")


def main():
    n = int(input())
    solve(n)


if __name__ == '__main__':
    main()
