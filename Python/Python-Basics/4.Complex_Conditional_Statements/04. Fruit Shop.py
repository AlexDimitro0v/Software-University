"""
The fruit prices in a shop are different according with the day of the week. During the weekend the prices are higher.

Input:
• The name of the fruit
• The day of the week
• The quantity to be bought.
Output:
• What is the price to be paid in regards to the quantity and the day of the week
    o If the inputted day of the week or the name of the fruit is invalid output "error"

Note: Format the result to 2nd decimal point.
"""

workdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
fruits = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']   # supported fruits


def get_price(day, fruit, quantity):
    fruits_week = {"banana": 2.50,
                   "apple": 1.20,
                   "orange": 0.85,
                   "grapefruit": 1.45,
                   "kiwi": 2.70,
                   "pineapple": 5.50,
                   "grapes": 3.85
                   }
    fruits_weekend = {"banana": 2.70,
                      "apple": 1.25,
                      "orange": 0.90,
                      "grapefruit": 1.60,
                      "kiwi": 3.00,
                      "pineapple": 5.60,
                      "grapes": 4.20
                      }
    if fruit in fruits_week and day in workdays:
        price = fruits_week[fruit] * quantity
    elif fruit in fruits_weekend and day in weekend:
        price = fruits_weekend[fruit] * quantity
    else:
        return "error"

    return f"{price:.2f}"


def display_price(day, fruit, quantity):
    if day in workdays:
        fruit_cost = {
            "banana": 2.50,
            "apple": 1.20,
            "orange": 0.85,
            "grapefruit": 1.45,
            "kiwi": 2.70,
            "pineapple": 5.50,
            "grapes": 3.85
        }

    elif day in weekend:
        fruit_cost = {
            "banana": 2.70,
            "apple": 1.25,
            "orange": 0.90,
            "grapefruit": 1.60,
            "kiwi": 3.00,
            "pineapple": 5.60,
            "grapes": 4.20
        }
    else:                       # if day not in workdays+weekend:
        print("error")
        return          # used as a function exit

    if fruit not in fruit_cost.keys():
            print('error')
            return      # used as a function exit
    else:
        for f, c in fruit_cost.items():
            if f == fruit:
                price = f"{quantity*c:.2f}"
                print(price)
                break


def main():
    # _____________________________________________Input
    fruit = input("Enter a fruit: ")
    day = input("Enter a day: ")
    quantity = float(input("Enter quantity: "))
    # _____________________________________________Input
    display_price(day, fruit, quantity)


if __name__ == '__main__':
    main()
