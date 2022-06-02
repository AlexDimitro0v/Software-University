# 17th April 2016 - SoftUni exam question.
"""
Pesho has bought some bitcoins not long ago, he also has some Chinese yuan. Now he is going on a holiday in Europe
and needs some Euros. He wants to exchange currencies and bitcoins, so that he can have euros for the holiday.
Calculate how much euros he can buy, following the currency rates below:
• 1 BT      = 1168 BGN
• 1 Yuan    = 0.15 USD
• 1 USD     = 1.76 BGN
• 1 EUR     = 1.95 BGN

Input(reading 3 numbers, one per line):
• The amount of bitcoins Pesho has
• The amount of Chinese yuan Pesho has
• The commission percent that the exchange house takes from the final EUR amount Pesho gets
Output:
• The final amount of EUR Pesho has bought
"""


def to_bgn(bitcoins, chinese_money):
    """
    :param bitcoins:      float
    :param chinese_money: float
    :return:              The total BGN amount Pesho has. (float)
    """
    # Bitcoins to BGN
    bt_bgn = bitcoins * 1168

    # Chinese money to BGN
    chn_usd = chinese_money * 0.15
    usd_bgn = chn_usd * 1.76

    return bt_bgn + usd_bgn


def to_eu(bgn):
    """
    :param bgn: the returned value from to_bgn function (float)
    :return: float
    """
    return bgn / 1.95


def commission(total_money, commission_rate):
    """
    :param total_money:      the total amount of EUR returned from the to_eu function (float)
    :param commission_rate:  the % of commission
    :return:                 the amount of discount on a certain total_price in EU
    """
    return total_money * commission_rate


def main():
    bitcoins = int(input("Enter the amount of bitcoins: "))
    chinese_money = float(input("Enter the amount of Chinese currency: "))
    commission_rate = float(input("Enter the commission rate: ")) / 100      # % of commission
    BGN = to_bgn(bitcoins, chinese_money)
    EUR = to_eu(BGN)
    commission_amount = commission(EUR, commission_rate)
    final_amount_in_eur = EUR - commission_amount
    print(f"The final amount in EUR is {final_amount_in_eur}")


if __name__ == '__main__':
    main()
