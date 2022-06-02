# Write a simple program to convert USD to BGN. Format the result to the 2nd decimal point.
dollars = float(input("Enter the amount in dollars: "))


def dollars_to_lv(usd):
    bgn = usd * 1.79549                                         # BGN= "%.2f" % (USD * 1.79549)
    return bgn


if __name__ == '__main__':
    # Different ways of formatting
    print(dollars, "USD to BGN = " "%.2f" % dollars_to_lv(dollars), "lv")
    print(f"{dollars} USD to BGN = {dollars_to_lv(dollars):.2f}lv")
    print("%.1f USD to BGN = %.2f lv" % (dollars, dollars_to_lv(dollars)))
