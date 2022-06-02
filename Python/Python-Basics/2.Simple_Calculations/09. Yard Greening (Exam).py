"""
Nancy has several houses on the Black Sea coast and wants to grass the yards of some of them, so that she can create
a cozy atmosphere and secure comfort for its guests, for this purpose she has rented a landscaping company.
Write a program that calculates the necessary funds that Bozhidara will have to pay to the project's contractor.
The price per square meter is 7.61BGN with VAT. Since her yards are quite large, the contractor offers an 18% discount
on the final price.
Input: Square meters that will be grassed/landscaped
Output:
•    The final price in BGN.
•    The total discount on the price in BGN
Format the results to the 2nd decimal point.
"""


def landscaping_price(total_space):
    total_price = total_space*7.61
    return total_price


def landscaping_discount(total_price):
    """Return the discount on a certain total_price in BGN"""
    return total_price*0.18


if __name__ == '__main__':
    final_price = landscaping_price(float(input()))
    discount = landscaping_discount(final_price)
    print(f"The final price is: {final_price-discount:.2f} lv.")
    print(f"The discount is: {discount:.2f} lv.")
