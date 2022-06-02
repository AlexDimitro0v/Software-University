"""
Ivan decides to spend his holiday skiing. However, before that he has to reserve a hotel and calculate how much it will
cost him. There are different types of rooms on a different price:
 "room for one person"     – 18.00BGN per night
 "apartment"               – 25.00BGN per night
 "president apartment"     – 35.00BGN per night

According with the days he is going to stay in the hotel and the type of room, there are different available discounts:
------------------------------------------------------------------------------------------------------------------------
                         10 days or less                        between 10 and 15 days                 more than 15 days
Room for one person  -     no discount                             no discount                           no discount
Apartment            -        30%                                      35%                                   50%
President Apartment  -        10%                                      15%                                   20%
------------------------------------------------------------------------------------------------------------------------

After the stay Ivan gives a feedback of the hotel services - if he is satisfied and gives a positive feedback, he adds
25% of the final price(with the already applied discount) as a tip. If Ivan is not satisfied and leaves a negative
feedback, 10% is deducted from the final price(with the already applied discount).

Input:
1. Days of stay
2. Type of room  - "room for one person", "apartment", "president apartment"
3. The feedback  - "positive" or "negative
Output:
• The total price he will pay, formatted to the 2nd decimal point.

Note: 5 days = 4 nights in the hotel !!!
"""


def discount(prices, room_type, nights):
    if nights < 10:
        discounts = {
            "room for one person": 0,
            "apartment": 0.3,
            "president apartment": 0.1
        }
    elif 10 <= nights <= 15:
        discounts = {
            "room for one person": 0,
            "apartment": 0.35,
            "president apartment": 0.15
        }
    else:                   # if nights > 15
        discounts = {
            "room for one person": 0,
            "apartment": 0.5,
            "president apartment": 0.2
        }
    return prices[room_type]*nights*discounts[room_type]


def hotel_tip(feedback, total_price):
    if feedback == 'positive':
        return total_price + total_price*0.25
    elif feedback == 'negative':
        return total_price - total_price*0.1
    else:
        print("Error")
        return


def main():
    prices = {
        "room for one person": 18,
        "apartment": 25,
        "president apartment": 35
    }

    nights = int(input()) - 1

    room_type = input()
    while room_type not in ["room for one person", "apartment", "president apartment"]:
        print("Enter the type of room accurately.")
        room_type = input()

    feedback = input()
    while feedback not in ['positive', 'negative']:
        print("Enter positive or negative as a feedback.")
        feedback = input()

    total_price = prices[room_type]*nights - discount(prices, room_type, nights)
    final_price = hotel_tip(feedback, total_price)
    print(f"{final_price:.2f}")


if __name__ == '__main__':
    main()
