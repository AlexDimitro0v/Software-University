def get_min(items):
    nums = []
    for i in items:
        nums += [int(i)]

    # minimum = 1000000000000
    minimum2 = nums[0]
    for number in nums:
        if number < minimum2:
            minimum2 = number

    return minimum2
    # _______________
    # another way with a built-in function
    # print(min(nums))


print(get_min(items=input().split(" ")))        # string.split(" ") splits string by space and produces a list
