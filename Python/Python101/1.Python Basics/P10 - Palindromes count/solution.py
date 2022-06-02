import time


def string_reverse(s):
    return ''.join(reversed(s))


def is_integer_palindrome(x):
    x = str(x)
    return x == string_reverse(x)


def is_palindrome(string):
    """Source: Aberdeen-Uni: 4.Marked Exercise (Palindromes)"""
    try:
        digits = str(string)
        return digits == digits[::-1]
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


def build_cache():
    # memoization
    cache = {}
    n = 99999
    for x in range(10, n + 1):
        cache[x] = is_palindrome(x)
    return cache


CACHE = build_cache()


def palindromes_count_fast(n):
    """
    Return the number of palindromes between 10 and n [10, n]
    10 <= n <= 99999
    """
    count = 0
    for i in range(10, n+1):
        if CACHE[i]:
            count += 1
    
    return count


def palindromes_count_slow(n):
    count = 0
    for i in range(10, n+1):
        if is_palindrome(i):
            count += 1
    
    return count


if __name__ == '__main__':
    tests = [
        (10, 0),
        (20, 1),         # only 11
        (30, 2),
        (101, 10),       # 11, 22, 33, 44, 55, 66, 77, 88, 99, 101
        (200, 19),
        (43539, 525),
        (4247, 132),
        (48877, 577),
        (94012, 1029),
        (62560, 715),
        (92009, 1009),
        (63176, 721),
        (67409, 763),
        (62834, 718),
        (77420, 863),
        (99999, 1089),
    ]
    
    start_time = time.time()
    for test, expected in tests:
        result = palindromes_count_fast(test)
        print(result == expected)
    print(f"--- {time.time() - start_time} seconds ---\n")
    
    start_time_2 = time.time()
    for test, expected in tests:
        result = palindromes_count_slow(test)
        print(result == expected)
    print(f"--- {time.time() - start_time_2} seconds ---")

