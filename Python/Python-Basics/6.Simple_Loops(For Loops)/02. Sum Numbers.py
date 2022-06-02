"""
Write a program that reads n number of integers (n>0) entered by the user and sums them.
Input:
• First Line - n (the number of integers to be entered from the user).
• The next n lines - a single integer per line.
Output:
• The total sum
Example:
    Input               Output
       2
      10
      20                  30
"""


def sum_numbers(n):
    total_sum = 0
    for num in range(1, n+1):
        num_input = int(input())
        total_sum = total_sum + num_input

    print(total_sum)                          # printing the last value of total_sum once


sum_numbers(int(input()))
