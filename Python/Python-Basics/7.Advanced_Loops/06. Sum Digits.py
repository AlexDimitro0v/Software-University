"""
Write a program that reads a number and outputs the sum of its digits. Ex: 19 -> 1+9=10
"""


def sum_digits(num):
    result = 0

    while num > 0:
        result += (num % 10)  # returns the last digit of n
        num = num // 10       # deletes the last digit of n
    print(result)


# another smarter way with casting
def sum_digits2():
    num = int(input())
    total_sum = 0
    for digit in str(num):
        total_sum += int(digit)
    print(total_sum)


# another way using a list
def sum_digits3(num):
    digits = [None] * len(str(num))        # creating an empty list with the length of the number

    for digit in range(0, len(str(num))):  # for the length of the number
        last_digit = int(num) % 10
        num = num // 10
        digits[digit] = last_digit         # stores each last number in the list

    print(sum(digits))


def main():
    num = int(input())
    sum_digits(num)


if __name__ == '__main__':
    main()
