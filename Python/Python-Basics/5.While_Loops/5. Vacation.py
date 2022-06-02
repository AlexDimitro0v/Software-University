"""
Jessie has to save money for a holiday. You should help her find out whether she can save enough money or not.
Jessie spends as well as saves money every day. Whenever she spends more money than the capital, she can ask her father
to give her cash, so that she never has a negative balance.

Input:
• Money needed for the holiday  (float)
• Owned money - capital         (float)
• Then repeatedly read:
    o Activity for the day - "spend" or "save"  (string)
    o The amount of money to be saved or spent  (float)
Output:
• If Jessie spends money 5 days in a row, print:
    o "You can't save the money."
    o "{Days passed}"
• If Jessie saves enough money for the holiday, print:
    o "You saved the money for {days} days."
"""


def solve(money_needed, capital):
    spending_days = 0
    days = 0
    while capital < money_needed:
        activity = input()
        amount = float(input())
        if activity == 'spend':
            spending_days += 1
            capital -= amount
            if capital < 0:
                capital = 0
        elif activity == 'save':
            spending_days = 0
            capital += amount
        days += 1

        if spending_days == 5:
            print("You can't save the money.")
            return days

    return f"You saved the money for {days} days."


def main():
    money_needed = float(input())
    capital = float(input())
    print(solve(money_needed, capital))


if __name__ == '__main__':
    main()
