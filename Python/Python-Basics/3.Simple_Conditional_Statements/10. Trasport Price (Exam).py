"""
A student has to travel n kilometers. He/She has a choice between 3 modes of transport:
1.Taxi
    o Starting fee -> 0.70
    o Daily tariff -> 0.79/km
    o Nightly tariff -> 0.90/km
2. Bus (available only for distance over 20km)
    o Daily/Nightly tariff -> 0.09/km
3. Train (available only for distance over 100km)
    o Daily/Nightly tariff -> 0.06/km

Write a program that reads the kilometers that the student has to travel and the day period (day or night) and finally
calculates the price of the cheapest mode of transport in accordance with the kilometers to be travelled.
"""


def calculate_cheapest_price(km, period):
    price = 0
    if km < 20 and period == "day":
        price = km * 0.79 + 0.70
    elif km < 20 and period == "night":
        price = km * 0.90 + 0.70

    if 20 <= km < 100:
        price = km * 0.09
    elif km >= 100:
        price = km * 0.06

    return price


def main():
    day_period = ['day', 'night']
    km = int(input("Enter kilometres: "))
    period = input("Enter day or night: ")
    while period not in day_period:
        period = input("Enter day or night, please: ")

    price = calculate_cheapest_price(km, period)
    print(f"The cheapest price is {price}")


if __name__ == '__main__':
    main()
