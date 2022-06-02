# 6th March 2016 - SoftUni exam question.
# Create a fortress


def fortress(n):
    pie = n//2                  # ^
    underscore = 2*n-(4+pie*2)
    space = 2*n - 2

    print('/' + '^'*pie + "\\" + '_'*underscore + '/' + '^'*pie + "\\")  # static line

    for rows in range(1, n-2+1):
        if rows == n-2:
            print('|' + ' ' * (pie+1) + '_' * underscore + ' ' * (pie+1) + "|")
        else:
            print('|' + ' ' * space + '|')

    print('\\' + '_'*pie + "/" + ' '*underscore + '\\' + '_'*pie + "/")  # static line


def main():
    n = int(input())
    fortress(n)


if __name__ == '__main__':
    main()
