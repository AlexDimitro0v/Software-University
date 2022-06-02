"""
Write a program to turn a number (from 1 to 7) into day of the week. If the inputted number is not in the given range,
print "Error".
"""


def day_of_the_week(day):
    week_day = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    # if 1 > day < 7:
    #    return "Error"

    if day in week_day:
        return week_day[day]
    else:
        return "Error"


def main():
    day = int(input())
    print(day_of_the_week(day))


if __name__ == '__main__':
    main()
