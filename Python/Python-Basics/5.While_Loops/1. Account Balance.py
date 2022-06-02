"""
Write a program that calculates how much money is in a bank account after you make a certain number of deposits.
Input:
• N - The number of deposits: integer
• The next N lines - the amount of money you deposit every time - float.
Output:
• For every deposit, print:
    o "Increase: {the amount of deposited money}"
• If the amount of the declared deposit is negative(you have to deposit some money, amount can't be less than 0), print:
    o "Invalid operation!" and exit the program without continuing with the remaining declared deposits.
• Finally, print:
    o "Total: {the final total amount of money in the account}"

Note: Format the final amount with 2 places after the decimal point.
"""


def solve(n):
    total = 0
    for i in range(n):
        amount = float(input())
        if amount >= 0:
            print(f"Increase: {amount:.2f}")
            total += amount
        else:
            print("Invalid operation!")
            return f"Total: {total:.2f}"
    return f"Total: {total:.2f}"


def main():
    payments = int(input())
    print(solve(payments))
    # Note: This task could be solved with a while loop, counter and a break statement


if __name__ == '__main__':
    main()
