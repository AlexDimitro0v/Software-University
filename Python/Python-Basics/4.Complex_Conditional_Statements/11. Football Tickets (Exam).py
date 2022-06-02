# 17th July 2016 - SoftUni exam question.
"""
When the tickets for the European Football Cup were released, the fans started buying. There were 2 categories of
tickets with different prices:
•	VIP – 499.99BGN.
•	Normal – 249.99BGN.
The fans have a certain budget and the number of fans buying tickets together determines the percent of the budget that
should be allocated for transport to the cash desks:
• From 1 to 4 fans - 75% of the budget.
• From 5 to 9 fans - 60% of the budget.
• From 10 to 24 fans - 50% of the budget.
• From 25 to 49 fans - 40% of the budget.
• 50 or more fans - 25% of the budget.
Write a program to calculate whether or not they can buy tickets for the selected categories with the rest of their
budget and how much money will they have after that or will they need.

Input:
• The budget (decimal number)
• The category that fans want to buy a ticker for - "VIP" or "Normal" (string)
• The number of people in the group (integer)
Output:
• If the budget is sufficient, print:
    o "Yes! You have {N} leva left." - N is the remaining of the group's money.
• If the budget is NOT sufficient, print:
    o "Not enough money! You need {M} leva." - where M is the amount that is short.

Note: Format the result ot the 2nd decimal point.

"""


def solve(budget, ticket, people):
    if 0 < people < 5:
        budget -= budget * 75 / 100
    elif 4 < people < 10:
        budget -= budget * 60 / 100
    elif 9 < people < 25:
        budget -= budget * 50 / 100
    elif 24 < people < 50:
        budget -= budget * 40 / 100
    elif people >= 50:
        budget -= budget * 25 / 100

    if ticket == "VIP":
        ticket_price = 499.99 * people
        budget_left = abs(budget - ticket_price)

    elif ticket == "Normal":
        ticket_price = 249.99 * people
        budget_left = abs(budget - ticket_price)
    else:
        print("Error!")
        return

    if budget >= ticket_price:
        print("Yes! You have {} leva left.".format("%.2f" % budget_left))
    else:
        print("Not enough money! You need {} leva.".format("%.2f" % budget_left))


def main():
    budget = float(input())
    ticket = input()
    people = int(input())
    solve(budget, ticket, people)


if __name__ == '__main__':
    main()
