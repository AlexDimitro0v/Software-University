def sum_of_digits(n: int):
    """Python solution """
    try:
        n = abs(n)
        digits = []
        for digit in str(n):
            digits.append(digit)
        return sum(map(int, digits))
    except:
        raise Exception("The function was given an incorrect data type.")


def sum_of_digits_2(n: int):
    """Classic solution"""
    n = abs(n)
    result = 0
    
    while n != 0:
        digit = n % 10     # get the last digit
        result += digit
        n = n // 10        # cut/remove the last digit | Note: this is not the standard division '/' but the modular one
    
    return result


if __name__ == '__main__':
    tests = [
        (1325132435356, 43),
        (123, 6),
        (6, 6),
        (-10, 1),
        (0, 0)
    ]
    
    for n, expected in tests:
        result = sum_of_digits(n)
        print(result == expected)
