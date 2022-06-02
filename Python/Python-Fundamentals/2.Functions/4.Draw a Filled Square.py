# num = int(input())
# length = 2*num


def upper_and_lower_part(n1):
    length = 2 * n1
    print('-' * length)


def middle(n2):
    length = 2 * n2
    for i in range(1, n2 - 1):
        print('-' + '\/' * ((length - 2) // 2) + '-')


def filled_square(n3):
    upper_and_lower_part(n3)
    middle(n3)
    upper_and_lower_part(n3)


filled_square(int(input()))

