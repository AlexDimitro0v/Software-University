"""
Three athletes finish between 1-50 seconds. Write a program that reads the finishing time of the athletes and
calculates their total finishing time in minutes:seconds. The seconds should be wth a leading zero.
Example:
Finishing times: 35, 45, 44   => Total finishing time: 2:04
"""
# Algorithm
# 1. Read input (seconds)
# 2. Sum input
# 3. Check if sum:
#       a:0-59
#       b:60-119
#       c:120-179
# 4. Check if seconds < 10 --> leading zero
# 5.    a: print minutes : 0 + seconds
#       b: print minutes : seconds


def find_minutes(total_time):
    return total_time//60   # in order to take only the minutes ==> cuts the fraction


def find_seconds(total_time):
    return total_time % 60  # in order to take only the seconds ==> the remainder


if __name__ == '__main__':
    contest1 = int(input("Finished for: "))
    contest2 = int(input("Finished for: "))
    contest3 = int(input("Finished for: "))

    sum_seconds = sum([contest1, contest2, contest3])
    
    minutes = find_minutes(sum_seconds)
    seconds = find_seconds(sum_seconds)

    if seconds < 10:
        print(str(minutes) + ':0' + str(seconds))
    else:
        print(str(minutes) + ':' + str(seconds))
