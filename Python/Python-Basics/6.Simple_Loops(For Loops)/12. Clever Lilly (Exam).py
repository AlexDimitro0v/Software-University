# 24th April 2016 - SoftUni exam question.
"""
Lilly is already N years old. For her birthday every year, she receives a gift. For odd birthdays(1,3,5..n) she receives
toys and for even birthdays(2,4,6..n) she receives money. For her second birthday she receives 10$ and this amount
increases by 10$ for each of her following even birthdays(2->10, 4->20, 6->30..etc.). Over the years, Lilly saves the
money. However, Lilly's brother takes 1$ from Lilly in every of the years she is receiving money as a birthday present.
Lilly sells all the toys she receives over the years for P leva and adds the money to the savings. Her idea is to spend
the saved money on a washing machine. Write a program that calculates how much money she has saved and whether they will
be enough for Lilly to buy a washing machine.

Input(reading 3 numbers, one per line):
• Lilly's age               - integer
• Washing's machine price   - decimal
• P(the price of every toy) - integer
Output:
• If the money is enough:
    o "Yes! {N}" - where N is the remaining money after the purchase
• If the money is not enough:
    o "No! {M}" - where M is the sum that is short.

Note: Format N and M with 2 places after the decimal point.
"""


def solve(age, washing_machine_price, toy_price):
    even_birthdays = 0
    toys = 0
    money = 0
    increasement = 0

    for birthday in range(1, age+1):
        if birthday % 2 == 1:
            # receives a toy
            toys += 1

        elif birthday % 2 == 0:
            # receives money
            even_birthdays += 1
            increasement = increasement + 10
            money += increasement

    money -= even_birthdays * 1.00
    toy_price = toy_price * toys
    total_sum = money + toy_price

    diff1 = abs(total_sum - washing_machine_price)
    diff1 = "%.2f" % diff1

    if total_sum >= washing_machine_price:
        print(f"Yes! {diff1}")
    else:
        print(f"No! {diff1}")


def main():
    age = int(input("Lily's age: "))
    laundry = float(input("Washing machine's price: "))
    toy_price = int(input("Toy's price: "))
    solve(age, laundry, toy_price)


if __name__ == '__main__':
    main()
