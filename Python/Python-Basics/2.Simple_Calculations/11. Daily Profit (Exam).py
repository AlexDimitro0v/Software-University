# 17th July 2016 - SoftUni exam question.
"""
Ivan is a programmer in an US company and works from home on an average of N days per month by earning
an average of M dollars a day. At the end of the year, Ivan receives a bonus equal to 2.5 monthly salaries. Also, a
25%-tax from what he has earned during the year is applied each year.
Write a program to calculate the net average earnings of Ivan per day in BGN as he spends his money in Bulgaria.
It is assumed that there are exactly 365 days in the year. The USD-BGN exchange rate will be read from the console.

Input(reading 4 numbers, one per line):
• The working days in every month of the year (assuming they are all the same every month)
• The money earned per day
• The USD-BGN exchange rate as a float number (1USD = X lv where X is the float number)
Output:
• The average earnings per day in BGN. Format the result to the 2nd decimal point.
"""


def calculate_monthly_salary(monthly_days_at_work, money_a_day):
    return monthly_days_at_work * money_a_day


def calculate_yearly_salary(monthly_salary):
    return (monthly_salary * 12) + (monthly_salary * 2.5)


def calculate_commission(yearly_salary):
    return yearly_salary * 0.25


if __name__ == '__main__':
    working_days_in_the_month = int(input())
    money_per_day = float(input())
    USD_BGN_rate = float(input())
    monthly_salary = calculate_monthly_salary(working_days_in_the_month, money_per_day)
    yearly_salary = calculate_yearly_salary(monthly_salary)
    commission = calculate_commission(yearly_salary)
    final_money_usd = yearly_salary - commission
    final_money_bgn = final_money_usd * USD_BGN_rate
    average_money_per_day = final_money_bgn / 365
    print(round(average_money_per_day, 2))
