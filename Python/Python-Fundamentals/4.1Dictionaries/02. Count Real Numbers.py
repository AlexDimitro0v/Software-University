def count_real_numbers(nums):
    counts = dict()
    nums.sort()

    for item in nums:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for num in sorted(counts.keys()):                      # .keys() returns a list of all the keys
        print(f"{num} -> {counts[num]} times")


def main():
    items = [float(e) for e in input().split(' ')]  	   # string.split(' ') splits string by space and produces a list
    # items = list(map(float,input().split()))             works the same
    count_real_numbers(items)


if __name__ == '__main__':
    main()

