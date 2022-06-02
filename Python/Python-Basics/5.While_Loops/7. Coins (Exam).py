"""
Manufacturers of vending machines would like to make their machines return as little coins of change as possible.
Write a program that reads the amount of change that has to be returned and calculates the fewest number of coins that
can be used to return the change.

Example:
1.23 = 4 coins  -> coin from 1eu, 20cents, 2cents and 1cent.
0.56 = 3 coins  -> coins from 50cents, 5cents and 1cent.
"""


def solve(money):
    money = int(money * 100)           # convert to cents
    coins_counter = 0

    while money > 0:
        if money >= 200:
            coins_counter += 1
            money -= 200
        elif money >= 100:
            coins_counter += 1
            money -= 100
        elif money >= 50:
            coins_counter += 1
            money -= 50
        elif money >= 20:
            coins_counter += 1
            money -= 20
        elif money >= 10:
            coins_counter += 1
            money -= 10
        elif money >= 5:
            coins_counter += 1
            money -= 5
        elif money >= 2:
            coins_counter += 1
            money -= 2
        elif money >= 1:
            coins_counter += 1
            money -= 1

    return coins_counter


def main():
    change = float(input())
    print(solve(change))


if __name__ == '__main__':
    main()


# 0.1
# 0.2
# 0.5
# 0.10
# 0.20
# 0.50
# 1
# 2
# --------
# 8 possible coins
