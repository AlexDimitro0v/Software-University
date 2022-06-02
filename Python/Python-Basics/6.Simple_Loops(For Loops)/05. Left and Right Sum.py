"""
Write a program that reads 2*n number of integers (n>0) entered by the user and checks if the sum of the first n numbers
(left sum) is equal to the sum of the second n numbers (right sum).

Input:
• First Line - n (the number of integers to be entered from the user).
• The next n lines (left half)  - a single integer per line.
• The next n lines (right half) - a single integer per line.
Output:
• If the 2 halves are equal, print
    o "Yes, sum = {the equal sum}".
• If the 2 halves are NOT equal, print
    o "No, diff = {the difference}".
"""


def halves_equality(n):
    sum1 = 0
    sum2 = 0

    for number in range(1, n+1):
        number_left = int(input())
        sum1 = sum1 + number_left
    for number1 in range(1, n+1):
        number_right = int(input())
        sum2 = sum2 + number_right

    '''another way (better time performance)
        for number in range(1, (n*2)+1):      in range(0, n*2) or just (n*2) works the same 
            current_number = int(input())
            if number <= n:
                sum1 = sum1 + current_number
            elif number > n: 
                sum2 = sum2 + current_number
    '''

    if sum1 == sum2:
        print(f"Yes, sum = {sum1}")
    else:
        diff = abs(sum1-sum2)
        print(f"No, diff = {diff}")


def main():
    n = int(input())
    halves_equality(n)


if __name__ == '__main__':
    main()
