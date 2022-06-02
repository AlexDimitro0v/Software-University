"""
Write a program that reads 2*n number of integers (n>0) entered by the user and checks if the sums of all pairs
(every 2 consecutive numbers form a pair) are equal.

Input:
• First Line - n (the number of integers to be entered from the user).
• The next n lines - a single integer per line.
• The next n lines - a single integer per line.
Output:
• If the sums of all pairs are equal, print
    o "Yes, value = {the equal value of all sums}".
• Otherwise, print
    o "No, maxdiff = {the max difference between any 2 consecutive pairs}".
"""


def equal_pairs(n):
    total_sum = 0
    diff = 0

    for num in range(n):        # counting from zero
        number1 = int(input())
        number2 = int(input())

        if num > 0:             # the second element/input num
            diff = abs(total_sum - (number1 + number2))
        total_sum = number1 + number2

    if diff == 0:
        print(f'Yes, value={total_sum}')
    elif not diff == 0:
        print(f'No, maxdiff={diff}')


def main():
    n = int(input())
    equal_pairs(n)


if __name__ == '__main__':
    main()
