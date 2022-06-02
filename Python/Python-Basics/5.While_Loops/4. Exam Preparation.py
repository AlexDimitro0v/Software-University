"""
George prepares himself for a Math exam. He solves a number of past exams exercises until he receives a command "Enough"
from his teacher. For every solved exercise, he gets a mark. The process should continue until he is told that the work
is 'enough'(as mentioned) or gets a certain number of unsatisfying marks. An unsatisfying mark is every mark less or
equal than 4.

Input:
• The allowed number of unsatisfying marks (int)
• Then repeatedly read:
    o The current exercise title           (string)
    o The mark for the current exercise    (int)
Output:
• If George receives the command "Enough", print:
    o "Average score: {the average grade}"                              (float)
    o "Number of problems: {the number of total exercises solved}"      (int)
    o "Last problem: {the name of the last exercise}"                   (string)
• If George reaches the maximum allowed number of unsatisfying marks, print:
    o "You need a break, {limit} poor grades."

Note: Format the average grade with 2 places after the decimal point.
"""


def solve(limit):
    work = input()
    fails = 0
    grades_total = 0
    counter = 0
    while work != 'Enough':
        grade = int(input())
        grades_total += grade
        if grade <= 4:
            fails += 1
        if fails == limit:
            print(f"You need a break, {limit} poor grades.")
            return
        last_work = work
        work = input()
        counter += 1
    average_grade = grades_total/counter
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {counter}")
    print(f"Last problem: {last_work}")


def main():
    limit = int(input())
    solve(limit)


if __name__ == '__main__':
    main()
