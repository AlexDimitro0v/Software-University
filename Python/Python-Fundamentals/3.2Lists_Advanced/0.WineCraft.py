# Description of the task and judge system:
# https://judge.softuni.bg/Contests/Practice/Index/425?fbclid=IwAR1WJ83LNxAX6nfOOyKsl7yA1RA7VcRj1Qvyc32X2X_LJh8-DDyLwHl3UzA#5


def growing(grapes, n):
    for times in range(n):
        grapes_copy = grapes.copy()
        for i in range(1, len(grapes)-1):
            if grapes[i-1] < grapes[i] > grapes[i+1]:       # Classified as greater grape
                grapes[i] += 1
                if grapes[i-1] > 0:
                    grapes[i-1] -= 1
                    grapes[i] += 1
                if grapes[i+1] > 0:
                    grapes[i+1] -= 1
                    grapes[i] += 1

    # Incrementing all grapes that has not been changed
    # ______________________________________________________
        for e in range(len(grapes)):
            if grapes_copy[e] == grapes[e]:     # if the value has not been changed
                if grapes[e] > 0:
                    grapes[e] += 1
    # ______________________________________________________


def solve(grapes, n):
    grapes_copy = grapes.copy()
    while len(grapes_copy) >= n:
        growing(grapes, n)
        grapes_copy = [e for e in grapes if e > n]      # filtering the list by removing the numbers less or equal to n
        for e in range(len(grapes)):
            if grapes[e] < n:
                grapes[e] = 0
    return ' '.join(map(str, grapes_copy))


def main():
    grapes = [int(e) for e in input().split()]
    n = int(input())
    print(solve(grapes, n))


if __name__ == '__main__':
    main()
