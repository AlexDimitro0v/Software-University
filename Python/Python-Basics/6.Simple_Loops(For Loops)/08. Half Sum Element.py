"""
Write a program that reads n number of integers (n>0) entered by the user and checks if there is a number among them
that is equal to the sum of all others numbers.

Input:
• First Line - n (the number of integers to be entered from the user).
• The next n lines - a single integer per line.
Output:
• If there is such a number, print
    o "Yes Sum = {the equal sum}".
• If there is NOT such a number, print
    o "No Diff = {the difference}".

Algorithm:
Calculate the sum of all numbers and find the biggest among them, then check for the condition to solve the task.
"""


def solve(n):
    maximum = float('-inf')
    total_sum = 0

    for disc_number in range(1, n+1):
        number = int(input())
        total_sum += number

        if number > maximum:
            maximum = number

    total_sum -= maximum
    diff = abs(total_sum - maximum)
    if total_sum == maximum:
        print("Yes Sum = {}".format(total_sum))
    else:
        print("No Diff = {}".format(diff))


# another way
def half_sum_element(n):

    numbers = [None] * n            # Creating an empty list
    for i in range(n):
        num = int(input())
        numbers[i] = num            # Storing each number in the list

    maximum = max(numbers)
    total_sum = sum(numbers)

    total_sum -= maximum            # Solution with subtracting the max number from the total sum

    if total_sum == maximum:
        print("Yes")
        print("Sum = {0}".format(total_sum))
    else:
        print("No")
        print("Diff = {0}".format(abs(total_sum - maximum)))


def main():
    n = int(input())
    solve(n)


if __name__ == '__main__':
    main()

