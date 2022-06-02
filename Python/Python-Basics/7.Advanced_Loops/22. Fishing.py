"""
Write a program to help your old friend George to calculate whether he returns from a fishing trip with a profit or loss
and also the amount of the profit/loss. Normally, every fish costs money, but every third fish caught is for free and
furthermore George receives money from this fish. The money that George is going to pay/receive for a fish is calculated
by finding the sum of the ASCII characters of the fish type and dividing it by the weight of the fish.

Input:
• The daily quota (the number of fishes that George can catch) - integer
• Then repeatedly until the quota is met or the command 'Stop' is received, read:
    o The fish type
    o The weight of the fish
Output:
• After the fishing, if George made a profit, print:
    o "George's profit from {fish caught} fishes is {the profit} leva."
• After the fishing, if George lost money, print:
    o "George lost {the total loss} leva today."

Note: Format the percents with 2 places after the decimal point.
"""


def solve(quota):
    fish_caught = 0
    cost = 0
    profit = 0
    for times in range(1, quota+1):
        fish_name = input()
        if fish_name == 'Stop':
            break
        letters_sum = 0
        weight = float(input())
        for letter in fish_name:
            letters_sum += ord(letter)
        price = letters_sum / weight
        if not times % 3 == 0:              # because every third fish for free
            cost += price
        else:
            profit += price
        fish_caught += 1
    if fish_caught == quota:
        print("George fulfilled the quota!")
    if profit >= cost:
        return f"George's profit from {fish_caught} fishes is {profit-cost:.2f} leva."
    else:
        return f"George lost {cost-profit:.2f} leva today."


def main():
    quota = int(input())
    print(solve(quota))


if __name__ == '__main__':
    main()
