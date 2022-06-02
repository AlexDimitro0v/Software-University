"""
You have a task to calculate the profit of a specific cinema. The cinema has just 1 cinema hall for projections.
The charis in the hall are arranged in a rectangular shops (r rows and c columns). There are 3 different types of
screening on a different price:
• Premiere - Premiere, at the price of 12.00BGN.
• Normal - Standard projection, at a price of 7.50BGN.
• Discount - Screening for children, pupils and students, at a reduced price of 5.00BGN.
Your program should read the type of the projection(string), the number of rows(int) and columns(int) in the hall and
calculate the total revenue from the tickets (assuming the hall is always full).

Note: Format the result to the 2nd decimal point
"""
types = {'Premiere': 12.00, 'Normal': 7.50, 'Discount': 5.00}


def rectangle_area(a, b):
    return a*b


def calculate_profit(film, rows, columns):
    income = 0
    hall_area = rectangle_area(rows, columns)
    if film == "Premiere":
        income = hall_area * 12.00
    elif film == "Normal":
        income = hall_area * 7.50
    elif film == "Discount":
        income = hall_area * 5.00
    else:
        print("error")

    print(f"{income:.2f}")


def calculate_profit2(film, rows, columns):     # another way
    if film in types:
        print(f"{types[film] * rows * columns:.2f}")
    else:
        print("error")


def main():
    film = input("Enter the type of the movie: ")
    rows = int(input())
    columns = int(input())
    calculate_profit(film, rows, columns)


if __name__ == '__main__':
    main()
