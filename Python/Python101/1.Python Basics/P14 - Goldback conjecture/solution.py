from itertools import combinations, combinations_with_replacement
"""
1. cartesian product, equivalent to a nested for-loop:
   product('ABCD', repeat=2)                  AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

2. R-length tuples, all possible orderings, no repeated elements:
   permutations('ABCD', 2)                    AB AC AD BA BC BD CA CB CD DA DB DC
   
3. R-length tuples, in sorted order, no repeated elements:
   combinations('ABCD', 2)                    AB AC AD BC BD CD

4. R-length tuples, in sorted order, with repeated elements:
   combinations_with_replacement('ABCD', 2)   AA AB AC AD BB BC BD CC CD DD
"""
# https://www.youtube.com/watch?v=PeUJzKFh2sQ&ab_channel=HackBulgaria


def goldbach_2(n):
    if n <= 2 or n % 2 == 1:
        return
    result = []
    # List comprehension
    primes = [x for x in range(2, n) if is_prime(x)]
    
    for p1, p2 in combinations_with_replacement(primes, 2):
        if p1 + p2 == n:
            result.append((p1, p2))
    return result


def is_odd(n):
    if n % 2 == 1:
        return True
    return False


def is_prime(n):
    if n < 2:
        return False
    square_root = int(n**1/2)
    for d in range(2, square_root+1):
        if n % d == 0:
            return False
    return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


def goldbach(n):
    try:
        if is_odd(n) or n <= 2:
            return
        primes_goldbach = []
        used = set()
        # primes = [x for x in range(2, n) if is_prime(x)]
        p1 = 2
        while p1 < n:
            p2 = 2
            while p2 < n:
                if n == p1+p2:
                    pair = (p1, p2)
                    reverse_pair = (p2, p1)
                    if pair not in used and reverse_pair not in used:
                        used.add(pair)                      # a+b == b+a
                        primes_goldbach.append((p1, p2))
                p2 = next_prime(p2)
            p1 = next_prime(p1)
            
        # print(list(primes_goldbach), end=' ')
        return list(primes_goldbach)
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


if __name__ == '__main__':
    tests = [
        (2, None),
        (4, [(2, 2)]),
        (6, [(3, 3)]),
        (8, [(3, 5)]),
        (10, [(3, 7), (5, 5)]),
        (100, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]),
        (5, None),
        (-1, None)
    ]
    
    for test, expected in tests:
        result = goldbach(test)
        print(result == expected, result)
