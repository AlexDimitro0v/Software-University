"""
Annie loves travelling and this year she wants to visit several countries. As soon as she picks a destination, she
estimates how much money she will need to go there and will start saving up. Once she got the money, she can travel.
Firstly, in your program, you will read the destination and the needed money. Then, you will repeatedly read the savings
she sets aside until she has enough money to travel to the destination - in this case, print: "Going to {destination}!".
Once she visits all the destinations she wants to go to, you will read 'End' from the console and terminate the program.
"""


def solve1(destination, money_needed):
    budget = 0

    action = input()            # once
    while action != 'End':
        try:
            budget += float(action)
            if budget >= money_needed:
                print(f"Going to {destination}!")
                budget = 0
        except ValueError:
            destination = action
            try:
                money_needed = float(input())
            except ValueError:
                return
        action = input()


def solve2(destination):
    while destination != 'End':
        money_needed = float(input())
        saved_money = 0
        while saved_money < money_needed:
            savings = float(input())
            saved_money += savings
        print(f"Going to {destination}!")
        destination = input()


def main():
    destination = input()
    if destination == 'End':
        return
    money_needed = float(input())
    solve1(destination, money_needed)


if __name__ == '__main__':
    main()
