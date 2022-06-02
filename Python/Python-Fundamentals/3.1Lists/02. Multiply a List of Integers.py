def play_around():
    # nums = [int(item) for item in input().split(' ')]   does the same on one line
    # filling an empty list with strings
    values = input()
    items = values.split(' ')

    # casting the string elements from a list to int
    nums = []     # 1.By creating a new empty list
    for i in items:
        nums += [int(i)]  # or nums.append(int(i))
    print(nums)

    index = 0     # 2.By modifying the existing list created by the split function
    for element in items:
        items[index] = int(element)
        index += 1
    print(items)


def multiply_list():
    nums = input().split()              # string.split(' ') splits string by space and produces a list
    nums = map(int, nums)               # map returns an iterator
    p = int(input())
    for every_item in nums:
        print(every_item * p, end=' ')  # here return won't work as it will stop the loop
    # alternatively, list comprehension:
    # nums = [x*p for x in nums]


multiply_list()

'''
print()
p = int(input())
for item in range(len(nums)):
    print(nums[item]*p,end=' )
'''

'''
directly printing every item from the list by multiplying it 

p = int(input())
for every_item in nums:
    print(every_item*p ,end=" ")

'''

'''
iterating through the whole list 
p = int(input())
for i in range(len(nums)):
    nums[i] = nums[i]*p
print(nums)

for item in nums:
    print(item, end=" ")
'''

'''
print()
nums2= []
p = int(input())
for every_item in nums:
    nums2 += [every_item*p]
print(nums2)
'''
