def fact_digits(n: int):
    try:
        n = abs(n)
        result = 0
    
        while n != 0:
            digit = n % 10  # get the last digit
            result += fact(digit)
            n = n // 10    # cut/remove the last digit | Note: this is not the standard division '/' but the modular one
        return result
    
    except:
        raise Exception("An incorrect input type was given.")


def get_fact(n: int):
    return 1 if (n == 1 or n == 0) else n * get_fact(n - 1)


def fact(n):
    result = 1
    
    for x in range(1, n + 1):
        result *= x
    
    return result


if __name__ == '__main__':
    tests = [
        (101, 3),
        (111, 3),
        (145, 145),
        (999, 1088640),
        (5, 120)
    ]
    
    for test, expected in tests:
        result = fact_digits(test)
        print(result == expected)
