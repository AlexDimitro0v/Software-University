def triangle_area(base, height):
    area = base * height / 2
    return area


# void function ______________________________________________
def print_triangle_area(base, height):
    area = base * height / 2
    print(f'{area:.12g}')


#  reading input in the function ______________________________
def triangle_area2():
    base = float(input())
    height = float(input())
    return base * height / 2


def main():
    base = float(input())
    height = float(input())
    area = (triangle_area(base, height))
    print(f'{area:.12g}')
    # print(f'{triangle_area(base,height):.12g}')  # works the same


if __name__ == '__main__':
    main()
