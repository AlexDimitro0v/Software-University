"""
Write a program that reads n number of integers (n>0) entered by the user and checks if the sum of the numbers at even
positions is equal to the sum of the numbers at odd positions.

Input:
• First Line - n (the number of integers to be entered from the user).
• The next n lines - a single integer per line.
Output:
• If the 2 sums are equal, print
    o "Yes Sum = {the equal sum}".
• If the 2 sums are NOT equal, print
    o "No Diff = {the difference}".
"""


def solve(n):
    sum1 = 0
    sum2 = 0
    for number in range(1, n+1):
        # num = int(input())
        if number % 2 == 0:
            number_odd = int(input())
            sum1 += number_odd
        else:
            number_even = int(input())
            sum2 += number_even

    dif = abs(sum1 - sum2)
    if sum1 == sum2:
        print(f"Yes Sum = {sum1}")
    else:
        print(f"No Diff = {dif}")


def main():
    n = int(input())
    solve(n)


if __name__ == '__main__':
    main()
