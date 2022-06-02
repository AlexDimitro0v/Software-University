# Probably if not the most difficult, one of the most difficult tasks in the course
"""
A student has to take an exam at a specific time (for example 9:30). He arrives in the exam room at a certain time
as well (for example 9:40). Write a program that calculates if the student arrives late, on time or too early and also
by how many hours and/or minutes late or earlier.

Input(reading 4 numbers, one per line):
• The exam starting hour    - integer between 0 and 23
• The exam starting minute  - integer between 0 and 59
• The arrival hour          - integer between 0 and 23
• The arrival minute        - integer between 0 and 59
Output:
1. On the First Line print:
    • "Late" if the student arrives later.
    • "On time" if the student arrives exactly on time or up to 30 minutes before the exam.
    • "Early" if the student arrives more than 30 minutes before the exam.
2. On the Second Line print:
    • If the student does NOT arrive exactly on time:
        o "mm minutes before the start"     for arriving earlier in less than an hour.
        o "hh:mm hours before the start"    for arriving 1 hour or more earlier.
        o "mm minutes after the start"      for being under an hour late.
        o "hh:mm hours after start"         for being late 1 or more hours.

Note: Always print the minutes with 2 digits - e.g 1:05 or 0:00
"""


def solve(exam_hour, exam_minute, arrival_hour, arrival_minute):
    total_minutes_exam = exam_hour*60 + exam_minute
    total_minutes_arrival = arrival_hour*60 + arrival_minute
    diff = abs(total_minutes_exam - total_minutes_arrival)
    hours = diff // 60      # extracting the hours
    minutes = diff % 60     # extracting the minutes
    if total_minutes_arrival > total_minutes_exam:      # being late
        print("Late")
        if diff < 60:
            print(f"{diff} minutes after the start")
        else:
            if minutes < 10:
                print(f"{hours}:0{minutes} hours after the start")
            else:
                print(f"{hours}:{minutes} hours after the start")
    else:  # ---------> # being on time or earlier
        if diff <= 30:  # if the student arrives exactly on time or max 30 minutes before the exam
            print("On Time")
        else:           # if diff > 30, i.e the student arrives more than 30 minutes before the exam
            print("Early")
        if diff == 0:   # if the student arrives exactly on time
            return
        elif diff < 60:
            print(f"{diff} minutes before the start")
        else:           # if the student arrive 60 or more minutes earlier
            if minutes < 10:
                print(f"{hours}:0{minutes} hours before the start")
            else:
                print(f"{hours}:{minutes} hours before the start")


def main():
    exam_hour = int(input())
    exam_minute = int(input())
    arrival_hour = int(input())
    arrival_minute = int(input())
    solve(exam_hour, exam_minute, arrival_hour, arrival_minute)


if __name__ == '__main__':
    main()
