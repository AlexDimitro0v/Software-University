"""
Write a program that reads a name of a product and outputs whether it is a vegetable, a fruit or unknown.
"""


def veg_or_fruit(product):
    fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
    vegetables = ["tomato", "cucumber", "pepper", "carrot"]

    if product in fruits:
        return "fruit"
    elif product in vegetables:
        return "vegetable"
    else:
        return "unknown"


def main():
    name = input("Enter the name of the food: ")
    print(veg_or_fruit(name))


if __name__ == '__main__':
    main()
