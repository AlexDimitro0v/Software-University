# Create a butterfly
# 26th March 2016 - SoftUni exam question.


def butterfly(n):
    # rows = 2*(n-2)+1
    # columns = 2*(n-2)-1
    # left_right = n-1
    stars = n-2
    print('*'*stars+'\\'+' '+'/'+'*'*stars)                     # static line

    for rows in range(1, ((n-3)//2)+1):
            print('-' * stars + '\\' + ' ' + '/' + '-' * stars)
            print('*' * stars + '\\' + ' ' + '/' + '*' * stars)

    print(' '*(n-1)+"@")

    print('*' * stars + '/' + ' ' + '\\' + '*' * stars)         # static line

    for rows in range(1, (n-3)//2+1):
        print('-' * stars + '/' + ' ' + '\\' + '-' * stars)
        print('*' * stars + '/' + ' ' + '\\' + '*' * stars)


def main():
    n = int(input())
    butterfly(n)


if __name__ == '__main__':
    main()
