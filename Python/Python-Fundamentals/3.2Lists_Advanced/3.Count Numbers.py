def count_numbers1(numbers):
    # Solution using a dictionary
    dic = {}
    for num in numbers:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    for key, item in sorted(dic.items()):
        print(f"{key} -> {item}")


# _________________________________________________________________________
# another way
def count_numbers2(numbers):
    numbers.sort()

    count = 1
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i + 1]:
            count += 1
        else:
            print(f"{numbers[i]} -> {count}")
            count = 1
    print(f"{numbers[-1]} -> {count}")          # printing the very last item as well


# _________________________________________________________________________
# another way

class Numbers:
    def __init__(self, number):
        self.number = number


def count_numbers3(numbers):
    # LEGB rules
    dic_nums = {}
    numbers.sort()

    def is_in_dic():
        if elem in dic_nums:
            dic_nums[ob.number] += 1
        else:
            dic_nums[ob.number] = 1

    for elem in numbers:
        ob = Numbers(elem)
        is_in_dic()

    print(dic_nums)


def main():
    numbers = list(map(int, input().split()))
    count_numbers2(numbers)


if __name__ == '__main__':
    main()
