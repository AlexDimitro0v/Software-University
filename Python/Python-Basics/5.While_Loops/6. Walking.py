"""
Alex has a healthy lifestyle and has a target of 10 000 steps walk each day. Some days, however, she feels very tired
and gets back home before completing the daily target. Write a program that repeatedly reads the steps Alex makes
during the day before she completes the target of 10 000 total steps - once the target is completed, print
"Goal reached! Good job!".
If she wants to go home before completing the target, she will say that she is "Going home" and walk back home. If she
doesn't manage to complete the target while walking back home, print "{the difference} more steps to reach goal."
"""


def solve():
    total_steps = 0
    while total_steps < 10000:
        steps = input()
        try:
            total_steps += int(steps)
        except ValueError:
            steps_to_home = int(input())
            total_steps += steps_to_home
            break
    if total_steps >= 10000:
        return "Goal reached! Good job!"
    else:
        return f"{10000-total_steps} more steps to reach goal."


if __name__ == '__main__':
    print(solve())
