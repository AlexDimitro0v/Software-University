"""
Write a program that simulates a currency converter, which supports the following currencies: BGN, USD, EUR, GBP.
Input:
1. Amount of money
2. BGN/USD/EUR/GBP (the currency to be converted)
3. BGN/USD/EUR/GBP (the converted currency)
Output:
The converted currency
"""

# Rates
USD = 1.79549
EUR = 1.95583
GBP = 2.53405
BGN = 1


# Solution using globals
def globals_solution():
    # https://www.programiz.com/python-programming/methods/built-in/globals
    # a Global symbol table stores all information related to the global scope of the program,
    # and is accessed in Python using globals() method.

    amount = float(input("Enter the amount of money: "))

    fr = input("Enter the currency to be converted: ")
    try:
        debug1 = globals()[fr]
    # if the currency is not defined in a global scope
    except KeyError:
        while fr not in globals():
            fr = input("Enter the currency to be converted - Use BGN/USD/EUR/GBP: ")

    to = input("Enter the wanted currency: ")
    try:
        debug2 = globals()[to]
    except KeyError:
        while to not in globals():
            to = input("Enter the currency to be converted - Use BGN/USD/EUR/GBP: ")

    try:
        amount = amount * globals()[fr] / globals()[to]
        # the money * the currency rate / currency rate of the wanted curr
    except KeyError:
        print("Error -.-")
    return str(round(amount, 2)) + ' ' + to

# __________________________________________________________________________


def currency_converter():
    supported_currencies = ['USD', 'EUR', 'GBP', 'BGN']
    amount = float(input("Enter the amount of money: "))

    curr = str(input("Enter the currency to be converted: "))
    while curr not in supported_currencies:
        curr = str(input("Enter the currency to be converted - Use BGN/USD/EUR/GBP: "))
    wanted_curr = str(input("Enter the wanted currency: "))
    while wanted_curr not in supported_currencies:
        wanted_curr = str(input("Enter the wanted currency - Use BGN/USD/EUR/GBP: "))

    USD = 1.79549
    EUR = 1.95583
    GBP = 2.53405

    # First step: Convert any currency to our base currency - Lv
    if curr == "USD":
        amount = amount * USD                   # To Lv
    elif curr == "EUR":
        amount = amount * EUR                   # To Lv
    elif curr == "GBP":
        amount = amount * GBP                   # To Lv

    if wanted_curr == "USD":
        amount = amount / USD
    elif wanted_curr == "EUR":
        amount = amount / EUR
    elif wanted_curr == "GBP":
        amount = amount / GBP

    return f"{round(amount,2)} {wanted_curr} "


if __name__ == '__main__':
    print(globals_solution())
