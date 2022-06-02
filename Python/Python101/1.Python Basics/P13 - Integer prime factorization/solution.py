# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def update_dict(dd, el):
    dd[el] = dd.get(el, 0) + 1


class PrimeFactorization:
    def __init__(self, n):
        self.factors = {}
        self.n = n

    def prime_numbers_generator(self):
        # https://stackoverflow.com/questions/567222/simple-prime-number-generator-in-python
        # https://code.activestate.com/recipes/117119/
        """ Generate an infinite sequence of prime numbers."""
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        q = 2   # The running integer that's checked for primeness
        while True:
            if q not in self.factors:     # q is a new prime.
                # Yield it and mark its first multiple that isn't already marked in
                # previous iterations.
                yield q   # not marked composite, must be prime
                self.factors[q * q] = [q]
            else:
                for p in self.factors[q]:   # move each witness to its next multiple
                    # If the key does not exist, insert the key, with the specified value
                    self.factors.setdefault(p + q, []).append(p)
                del self.factors[q]         # no longer need D[q], free memory
            q += 1
    
    def update_dict(self, factor):
        self.factors[factor] = self.factors.get(factor, 0) + 1
    
    def prime_factors_pairs(self):
        """
        'Prime Factorization' is finding which prime numbers multiply together to make
        the original number.
        """
        i = 2
        while i * i <= self.n:
            if self.n % i:    # if there is a remainder, cannot be divided
                i += 1
            else:
                self.n //= i
                update_dict(self.factors, i)    # getting some function from utils
        if self.n > 1:
            update_dict(self.factors, self.n)   # getting some function from utils
    
        print(f"{self.n} -> {self.factors}", end=' ')
        return [(key, value) for key, value in self.factors.items()]


class PrimeFactorization_2:
    def __init__(self, n):
        self.factors = []
        self.n = n
    
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        square_root = int(n**1/2)
        for d in range(2, square_root+1):
            if n % d == 0:
                return False
        return True
    
    def next_prime(self, n):
        n += 1
        while not self.is_prime(n):
            n += 1
        return n
    
    def prime_factors_pairs(self):
        p = 2
        n = self.n
        while n > 1:
            a = 0
            while n % p == 0:
                a += 1
                n = n // p
            
            if a > 0:
                self.factors.append((p, a))
            p = self.next_prime(p)
            
        print(f"{self.n} -> {self.factors}", end=' ')
        return self.factors
        
        
if __name__ == '__main__':
    tests = [
        (8, [(2, 3)]),
        (2, [(2, 1)]),
        (4, [(2, 2)]),
        (10, [(2, 1), (5, 1)]),
        (14, [(2, 1), (7, 1)]),
        (356, [(2, 2), (89, 1)]),
        (89, [(89, 1)]),            # 89 is a prime number
        (1000, [(2, 3), (5, 3)]),
    ]
    
    for test, expected in tests:
        prime_factor_object = PrimeFactorization_2(test)
        result = prime_factor_object.prime_factors_pairs()
        print(result == expected)
