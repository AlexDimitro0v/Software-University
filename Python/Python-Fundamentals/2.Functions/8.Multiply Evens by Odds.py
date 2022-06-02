def sum_of_evens(num):
    even_sum = 0
    # num = int(input())
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
    return even_sum


def sum_of_odds(num):
    odd_sum = 0
    # num = int(input())
    for digit in str(num):
        if int(digit) % 2 == 1:
            odd_sum += int(digit)
    return odd_sum


def multiply_evens_by_odds(number):
    return sum_of_evens(number) * sum_of_odds(number)


print(multiply_evens_by_odds(abs(int(input()))))
