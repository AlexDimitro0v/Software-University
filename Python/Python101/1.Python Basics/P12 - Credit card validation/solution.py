from collections import deque


def sum_digits(number: int):
    total_sum = 0
    while number != 0:
        total_sum = total_sum + (number % 10)    # add the last digit to the sum
        number = number//10                      # remove the last digit
    return total_sum


def is_credit_card_valid_1(number):
    """
    Algorithm:
    1. Take the original number and starting from the rightmost digit moving left, double
    the value of every second digit
    2. Replace the resulting value at each position with the sum of the digits of this
    position's value
        • If after doubling the digit becomes >= 10, calculate the sum of the digits of
          the new number & use that. For example, if we have 9 and doubling it gets us
          18, the final result is going to be 1+8=9
    3. Sum up the resulting values from all positions --> s
    4. The number is valid, if the sum is divisible by 10.
    """
    # Example:   79927398713
    # Total sum: 7 + 9 + 9 + 4 + 7 + 6 + 9 + 7 + 7 + 2 + 3
    try:
        total_sum = 0
        for index, digit in enumerate(reversed(str(number))):
            if index % 2 == 1:
                total_sum += sum_digits(int(digit)*2)
            else:
                total_sum += int(digit)
        print(total_sum, end=" ")
        return total_sum % 10 == 0
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


def is_credit_card_valid_2(number):
    digits = deque(map(int, str(number)))
    counter = 1
    for i in range(len(digits)):
        if counter == 2:
            num = sum_digits(digits.pop() * 2)
            counter = 1
        else:
            num = digits.pop()
            counter += 1
        digits.appendleft(num)
    print(sum(digits), end=" ")
    return sum(digits) % 10 == 0


# Example:   79927398713
# Total sum: 7 + 9 + 9 + 4 + 7 + 6 + 9 + 7 + 7 + 2 + 3
def is_credit_card_valid_3(number):
    """
    Extremely interesting pattern with overriding the value of a boolean (rotative)
    bool = not bool (редуване)
    Avoiding the even & odd position check makes the solution more readable
    """
    total_sum = 0
    digits = [int(s) for s in str(number)]
    digits_count = len(digits)
    double = False
    
    # range(start, end_non_inclusive, step)
    for index in range(digits_count-1, -1, -1):   # backtracking on to the reversed list
        multiplier = 2 if double else 1
        transformed = sum_digits(digits[index]*multiplier)
        total_sum += transformed
        double = not double         # TODO: Use this more often
        
    return total_sum % 10 == 0
    

if __name__ == '__main__':
    tests = [
        (79927398713, True),
        (4417123456789113, True),
        (4242424242424242, True),
        (79927398715, False),
        (79927398710, False),
        (79927398711, False),
        (79927398712, False),
        (79927398714, False),
        (79927398715, False),
        (79927398716, False),
        (79927398717, False),
        (79927398718, False),
        (79927398719, False)
    ]

    for test, expected in tests:
        result = is_credit_card_valid_3(test)
        print(result == expected)
