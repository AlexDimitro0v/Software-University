# 24th April 2016 - SoftUni exam question.
"""
Tom is a cat. He loves playing with his owner, but unfortunately his owner doesn't have much free time. In order Tom to
be happy he has to play at least 30 000 minutes during the year. Tom's playing time depends on his owner's free time:
• When his owner is at work, he plays with him 63 minutes a day.
• When his owner rests, he plays with him 127 minutes a day.
Assuming every year has 365 days, write a program that reads the free days of the owner in the year and outputs
whether Top is happy (i.e played enough during the year) and how much is the difference from the norm for the current
year (if there is one).
"""


def main():
    rest_days = int(input("Enter the rest days: "))
    working_days = 365 - rest_days
    norm = 30000
    play_time = (63 * working_days) + (127 * rest_days)
    find_norm_difference(norm, play_time)


def find_norm_difference(norm, play_time):
    norm_differ = abs(norm-play_time)
    hours = norm_differ // 60
    minutes = norm_differ % 60
    if play_time > norm:
        print("Tom is happy")
        print(f"{hours} hours and {minutes} minutes more for play")

    elif play_time < norm:
        print("Tom will run away")
        print(f"{hours} hours and {minutes} minutes less for play")


if __name__ == '__main__':
    main()
