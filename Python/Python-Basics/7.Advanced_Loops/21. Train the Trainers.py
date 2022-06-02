"""
The course 'Train the trainers' is towards is end and the final assessment is approaching. Write a program to help the
jury to assess the students. Your program should calculate the average score of every presentation of a given student
and finally the average score of all presentations that student presented.

Input:
• N - The number of people in the jury - integer
• Then repeatedly until the command 'Finish' is received, read:
    o The name of the current presentation
        • Finally, for every presentation, read:
            o as many grades as the number of people in the jury
Output:
• For the current presentation, print:
    o "{presentation} - {average grade}."
• After all presentations (once the command 'Finish' is entered), print:
    o "Student's final assessment is {average total grade)}."

Note: Format all results to the 2nd decimal point.
"""


def solve(judges):
    presentation = input()
    marks_total = 0
    presentations_number = 0
    while presentation != 'Finish':
        grade_total = 0
        for times in range(judges):
            grade = float(input())
            grade_total += grade
            marks_total += grade
        presentations_number += 1
        average_grade = grade_total / judges
        print(f"{presentation} - {average_grade:.2f}.")
        presentation = input()
    print(f"Student's final assessment is {marks_total/(judges*presentations_number):.2f}.")


def main():
    judges = int(input())
    solve(judges)


if __name__ == '__main__':
    main()
