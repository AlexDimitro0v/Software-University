"""
Write a console program that reads a score of points and output the total score when the following bonus points are
applied in accordance to the initial score.
• If the initial score is up to 100 inclusive, the bonus points are 5.
• If the initial score is greater than 100, the bonus points are 20% of the initial score.
• If the initial score is greater than 1000, the bonus points are 10% of the initial score.
• Additional bonus points (applied separately from the previous ones):
    o For an even number  + 1 pts.
    o For a number that ends with 5  + 2 pts.

Input:
• Score (Integer)
Output:
• The total points including the bonus points
"""


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def apply_bonus_points(score):
    bonus = 0
    if score <= 100:
        bonus += 5
    elif score > 1000:
        bonus += score*0.10
    elif score > 100:
        bonus += score*0.20
        
    if is_even(score):
        bonus += 1
    elif score % 10 == 5:
        bonus += 2
    
    return bonus


if __name__ == '__main__':
    points = int(input("Enter the points: "))
    bonus_points = apply_bonus_points(points)

    print(bonus_points)
    print(points + bonus_points)
