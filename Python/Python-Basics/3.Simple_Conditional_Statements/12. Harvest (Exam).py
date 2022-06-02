"""
From a vineyard with an area of X sq.m, 40% of the harvest is allocated for wine production.
From 1sq.m of vineyard, you earn Y kilos of grapes.
For 1 litres of wine, you need 2.5kg of grapes. The desired amount of wine to be sold is Z litres.
Write a program that calculates how much wine can be produced and if the quantity is enough.
If enough, the remainder is divided equally between the workers of the vineyard.

Input(reading 4 numbers, one per line):
• X sq.m of vineyard (floating point number)
• Y kilos of grapes for 1sq.m (floating point number)
• Z litres of target wine to be produced and then sold
• number of workers, working in the vineyard
Output:
• If the produced wine is less than desired, print
    o "It will be a tough winter! More {insufficient wine} liters wine needed." and round down the number.
• If the produced wine is more than necessary, print
    o "Good harvest this year! Total wine: {total wine} liters." and round down the number.
    o "{Left Wine} liters left -> {wine for 1 worker} liters per person." and round up both numbers.
"""
import math


def main():
    area = int(input("Enter the length of the vineyard: "))
    grapes = float(input("Enter grapes for 1m: "))                  # Grapes for 1m * total area
    wanted_wine = int(input("Enter litres of wine: "))              # Litres wanted
    number_of_workers = int(input("Enter number of workers: "))
    produced_wine = calculate_wine(area, grapes)
    solve(produced_wine, wanted_wine, number_of_workers)


def calculate_wine(area, grapes):
    wine = (0.40 * area) * grapes / 2.5  # litres to be produced
    return wine


def solve(wine, wanted_wine, number_of_workers):
    wine_diff = abs(wine - wanted_wine)
    if wine >= wanted_wine:
        wine_per_person = wine_diff / number_of_workers
        print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
        print(f"{math.ceil(wine_diff)} liters left -> {math.ceil(wine_per_person)} liters per person.")

    elif wine < wanted_wine:
        print(f"It will be a tough winter! More {math.floor(wine_diff)} liters wine needed.")


if __name__ == '__main__':
    main()
