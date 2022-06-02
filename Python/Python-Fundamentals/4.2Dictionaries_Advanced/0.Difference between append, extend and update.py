# Difference between append, extend and update

nums = [1, 2, 3, 4, 5]
even_nums = [6, 8, 10]

my_dict = {'lol': 98}
dic_more_nums = {'alex': 99, 'aya': 98}

nums.extend(even_nums)  # equal to                    nums += even nums
print(nums)             # [1, 2, 3, 4, 5, 8, 10]      nums shouldn't be added as a list as it is already a list

nums.append(
    even_nums
    )                   # adds a list to a list....equal to             nums += [even nums]
print(nums)             # [1, 2, 3, 4, 5, 8, 10, [6, 8, 10]]

my_dict.update(dic_more_nums)  # appending key:value pairs in a dic
print(my_dict)                 # {'lol': 98, 'alex': 99, 'aya': 98}

# _______________________________________________________________________________________________________
# Common Gotchas:
print()
list1 = ['1']
list2 = []
list3 = []
list4 = list()

list4.append(['alex', 'allan'])     # no need for append when adding a list        extend should be used in this case
list2 += 'alex'                     # no second element (take 'alex' as a list)    append should be used in this case
list2.extend('allan')               # extend with a single element will do the same as the line above

list1 += ['alex', 'allan']          # proper way of adding an existing list -> [1, 'alex', 'allan']
list3 += 'alex', 'allan'            # the same as the line above

print(list4)
print(list1)
print(list3)
print(list2)
