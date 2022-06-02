"""
Write a program that calculates the average school grade of a student who is graduating (assuming he/she spends 12 years
at school in order to graduate). You will read his/her name from the console, as well as his/her annual average grade
for the corresponding school year.
If the annual average grade is less than 4 (2 to 6 school grading system - 6 being the highest), they will repeat the
school year. If the student fails more than once, they will be excluded from school.

Output:
• Upon successful completion of the 12th grade, i.e the student graduates successfully, print:
    o "{Student name} graduated. Average grade: {average diploma grade}"
• If the student is excluded, print:
    o {Student name} has been excluded at {the grade he/she has been excluded at} grade"

Note: Format the average grade with 2 places after the decimal point.
"""


def average_diploma_grade(name):
    grade_sum = 0
    counter = 1
    fails = 0
    while counter <= 12:
        grade = float(input())
        if grade >= 4:
            grade_sum += grade
            counter += 1
        else:
            fails += 1
            if fails > 1:
                return f"{name} has been excluded at {counter} grade"

    return f"{name} graduated. Average grade: {grade_sum/12:.2f}"


def main():
    name = input()
    print(average_diploma_grade(name))


main()
