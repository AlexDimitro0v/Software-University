# Write a program that calculates the factorial of n, e.g if n=4 => 1*2*3*4


def fac(n):
    fac = 1  # A variable, the value of which will change constantly
    for num in range(1, n+1):
        # print(fac, k)
        fac *= num  # (1*2*3*4*5)              # Change the value of sum
    return fac


# __________________________________________________________________________________
# another way - while loop solution
def solve2(n):
    fact = 1
    while n > 1:
        fact = fact * n  # (5*4*3*2)
        n -= 1

    print(fact)


# __________________________________________________________________________________
# another way
def solve3(n):
    total_sum = n
    for k in range(1, n):
        total_sum = total_sum * k  # (5*1= 5*2= 10*3= 30*4= 120)
    print(total_sum)


# __________________________________________________________________________________
# another way - decreasing for loop (with a negative step)
def solve4(n):
    result = 1
    for num in range(n, 0, -1):
        result *= num  # 1*5= 5*4= 20*3= 60*2= 120   (5*4*3*2*1)
    print(result)


def main():
    n = int(input())
    print(fac(n))


if __name__ == '__main__':
    main()
