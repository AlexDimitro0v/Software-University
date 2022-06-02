"""
Write a program that reads hours and minutes of a 24-hour day and calculates what the time is after 15 minutes.
Print the result in hh:mm format. Hours are always between 0 and 23 and minutes are always between 0 and 59.
Hours are written in one or two digits. Minutes are always written in two digits, with leading zero when needed.
"""


def after_15_minutes(h, m):
    if m > 59:
        h = h + 1
        m = m - 60
    if h > 23:
        h = h - 24
    print(str(h), end=':')
    if m < 10:
        print('0', end='')
    print(m)


if __name__ == '__main__':
    hour = int(input("Enter hour: "))
    minutes = int(input("Enter minutes: ")) + 15
    after_15_minutes(hour, minutes)
