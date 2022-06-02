"""
Students can apply for a social scholarship or a scholarship for excellency at school.
Social scholarship requirements: income of a family member less than the minimum wage and school average grade over 4.50
The social scholarship is 35% of the minimum wage.
Excellency scholarship requirements: average grade >= 5.50. The scholarship is the student's average grade * 25.
Write a program that reads the student's parent's lowest salary, student's average grade and the minimum wage.
In accordance with the input give information whether the student has the right to receive a scholarship and the value
of the corresponding scholarship if applicable.

Input(reading 3 numbers, one per line):
• Income in BGN (float)
• Average grade(float)
• Minimum wage (float)
Output:
• If the student does not have the right to receive a scholarship, print
    o "You cannot get a scholarship!"
• If the student can get only the social scholarship, print
    o "You get a Social scholarship {amount of money} BGN"
• If the student can get only the excellency scholarship, print
    o "You get a Social scholarship {amount of money} BGN"
"""


def apply_scholarship(income, grade, minimum_salary):
    social = 0
    success = 0
    message = None
    if not (social_scholarship(income, minimum_salary, grade) or excellency_scholarship(grade)):
        message = "You cannot get a scholarship!"
    if social_scholarship(income, minimum_salary, grade):
        social = 0.35*minimum_salary
        message = f"You get a Social scholarship {int(social)} BGN"
    if excellency_scholarship(grade):
        success = grade * 25
        message = f"You get a scholarship for excellent results {int(success)} BGN"
    if excellency_scholarship(grade) and social_scholarship(income, minimum_salary, grade):
        if social > success:
            message = f"You get a Social scholarship {int(social)} BGN"
        else:
            message = f"You get a scholarship for excellent results {int(success)} BGN"

    return message


def social_scholarship(income, minimum_salary, grade):
    if income > minimum_salary:
        return False
    if grade < 4.5:
        return False
    return True


def excellency_scholarship(grade):
    if grade >= 5.5:
        return True
    return False


def main():
    income = float(input())
    grade = float(input())
    minimum_salary = float(input())
    print(apply_scholarship(income, grade, minimum_salary))


if __name__ == '__main__':
    main()
