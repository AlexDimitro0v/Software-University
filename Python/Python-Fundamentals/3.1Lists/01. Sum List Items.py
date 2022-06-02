def sum_list_items():
    n = int(input())
    total_sum = 0
    for i in range(n):
        num = int(input())
        total_sum += num
    return total_sum


# another way
# _________________________________
def sum_list_items2(n):
    total_sum = []
    for i in range(n):
        num = int(input())
        total_sum += [num]            # stores every input in a list
        # total_sum.append(num)       works the same as the line above
    return sum(total_sum)


def main():
    n = int(input())
    print(sum_list_items2(n))


if __name__ == '__main__':
    main()
