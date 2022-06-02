"""
Vladi is a student - he lives in Sofia and from time to time he travels to his hometown. He's very keen on Volleyball,
but he is busy during the week and plays only on weekends and holidays.
He plays in Sofia every Saturday (when he is not at work and does not travel to his hometown),
as well as in 2/3 of the holiday days. He travels to his hometown h times in the year and he plays Volleyball there
on Sunday with his old friends. Vladi is not at work 3/4 of the weekends he's in Sofia.
Furthermore, during the leap years Vladi plays 15% more Volleyball than usual.
Assuming there are exactly 48 weekends in the year suitable for Volleyball, write a program that calculates how many
times during the year Vladi has played Volleyball.

Input:
• Type of year - leap or normal (string)
• Number of holiday days in the year - only weekdays (integer)
• The h time Vladi travels to his hometown (integer)
Output:
• The times Vladi has player volleyball during the year.

Note: The result should be rounded down (For example -> 6.98 = 6.)
"""
import math


def leap_year_volleyball(volleyball, year):
    if year == "leap":
        volleyball += volleyball * 15 / 100
    elif year == "normal":
        pass
    else:
        print("error")
        return
    return volleyball


def main():
    year = input("Leap or normal: ")
    holiday_games = int(input("Enter the holiday days: ")) * 2/3
    weekends_home_games = int(input("Enter the amount of weekend days: "))
    weekends_sofia_games = (48 - weekends_home_games) * 3/4
    volleyball = holiday_games + weekends_sofia_games + weekends_home_games
    print(math.floor(leap_year_volleyball(volleyball, year)))


if __name__ == '__main__':
    main()
