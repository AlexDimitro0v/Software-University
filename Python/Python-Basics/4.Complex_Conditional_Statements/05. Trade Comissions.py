"""
A company gives commissions to their employees according with the town they work at and the number of sales
they have made.
Write a program that reads the name of the city and the number of sales made (decimal number) and calculates the amount
of the commission. Print "error" if the name of city is not Sofia, Varna or Plovdiv and the number of sales is a
negative number.

Note: Format the result to the 2nd decimal point.
"""


def calculate_commission(town, s):
    if town not in ['Sofia', 'Varna', 'Plovdiv']:
        return 'error'
    elif town == 'Sofia':
        comm = [5, 7, 8, 12]
    elif town == 'Varna':
        comm = [4.5, 7.5, 10, 13]
    elif town == 'Plovdiv':
        comm = [5.5, 8, 12, 14.5]

    if s < 0:
        return "error"
    if s <= 500:
        coefficient = 0
    elif s <= 1000:
        coefficient = 1
    elif s <= 10000:
        coefficient = 2
    else:
        coefficient = 3

    return f"{s*comm[coefficient]/100:.2f}"


def main():
    town = input("Enter a town: ")
    sales = float(input("Enter the amount of sales: "))
    print(calculate_commission(town, sales))


if __name__ == '__main__':
    main()
