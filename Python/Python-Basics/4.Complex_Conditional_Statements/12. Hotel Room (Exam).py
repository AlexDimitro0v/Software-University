"""
A hotel offers 2 types of rooms: studio and apartment. Write a program that calculates the price for the total stay in
the corresponding type of room.
Prices per night:
------------------------------------------------------------------------------------------------------------------------
            May and October                         June and September                      July and August
Studio    -     50BGN                                   75.20BGN                                76BGN
Apartment -     65BGN                                   68.70BGN                                77BGN
------------------------------------------------------------------------------------------------------------------------

The following discounts are available:
• For a studio with more than 7 nights in May and October: 5% discount.
• For a studio with more than 14 nights in May and October: 30% discount.
• For a studio with more than 14 nights in June and September: 20% discount.
• For an apartment, for more than 14 nights, regardless of the month: 10% discount.

Input:
• The month (May, June, July, August, September or October)
• The days of stay (integer)
Output:
On the first Line - "Apartment: {total price} lv."
On the second Line - "Studio: {total price} lv."

Note: Format the price to the 2nd decimal point.
"""


def solve(month, nights):
    studio = [50, 75.20, 76]
    apartment = [65, 68.70, 77]

    if month == "May" or month == "October":
        if nights > 14:
            studio_price = studio[0] - studio[0] * 30/100
            apartment_price = apartment[0] - apartment[0] * 10/100
        elif nights > 7:
            studio_price = studio[0] - studio[0] * 5/100
            apartment_price = apartment[0]
        else:
            studio_price = studio[0]
            apartment_price = apartment[0]

    elif month == "June" or month == "September":
        if nights > 14:
            studio_price = studio[1] - studio[1] * 20 / 100
            apartment_price = apartment[1] - apartment[1] * 10 / 100
        else:
            studio_price = studio[1]
            apartment_price = apartment[1]

    elif month == "July" or month == "August":
        if nights > 14:
            apartment_price = apartment[2] - apartment[2] * 10 / 100
            studio_price = studio[2]
        else:
            studio_price = studio[2]
            apartment_price = apartment[2]
    else:
        print("Error!")
        return

    print("Apartment: {} lv.".format("%.2f" % (apartment_price * nights)))
    print("Studio: {} lv.".format("%.2f" % (studio_price * nights)))


def main():
    month = input()
    nights = int(input())
    solve(month, nights)


if __name__ == '__main__':
    main()
