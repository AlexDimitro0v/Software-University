# https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/ - MUST SEE
# https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747   - Very helpful
# https://realpython.com/pointers-in-python/                                         - MUST SEE
# https://www.youtube.com/watch?v=AaIdperUu-A&ab_channel=JohnPhilipJones

from copy import copy, deepcopy


# Immutable objects(Float, Int, String, Tuples):
def fun(a, b, c):
    a = c - b
    b = c - 1
    print(a, b, c)


a = 2
b = 4
c = 8
fun(a, b, b + c)
print(a, b, c)          # The initial values of a, b and c are unchanged


print('-'*25)
a = 5
# print(id(a))
b = 6

b = a
print(id(a), id(b))

a += 1              # Now a occupy a different address in the memory
# print(id(a))
print('а =', a)
print('b =', b)     # B is unchanged
print('-'*25)


# _______________________________________________________________________________________________
# Mutable objects(Lists, Dictionaries, Sets) v.1:
my_list_1 = [1, 2, 3]
my_list_2 = [4, 5, 6]
# print(id(my_list_1), id(my_list_2))   different id's

my_list_1 = my_list_2    # list2 is assigned to list1
my_list_2[0] = 100       # changing the value of the 1st element in the list

print(my_list_1)
print(my_list_2)         # both lists are changed, because they are mutable and occupy the same address in the memory
# print(id(my_list_1), id(my_list_2))   same id's

# ___________________________________________________________________________________________________
# Mutable objects(Lists, Dictionaries, Sets) v.2:
initial_list = [1, 2, 3]


def duplicate_last(a_list):
    last_element = a_list[-1]
    a_list.append(last_element)
    return a_list


new_list = duplicate_last(a_list=initial_list)
print(new_list)      # [1, 2, 3, 3]
print(initial_list)  # [1, 2, 3, 3]
print('-'*25)


# __________________________________________________________________________________________________________________
# Keeping mutable data unchanged
lst1 = [1, 2, 3]
lst2 = list(lst1)       # playing the role of .copy()
lst3 = lst2.copy()
print(f"lst1: {lst1}\nlst2: {lst2}\nlst3: {lst3}")
lst1[0] = 100
lst2[0] = 1000
print(f"\nlst1: {lst1}\nlst2: {lst2}\nlst3: {lst3}")
print('-'*25)

list = ['abc', 123, 'xyz']
list1 = list[:]
list2 = list
list1.append(456)
list2.append('789')
print(f"list: {list}\nlist1: {list1}\nlist2: {list2}")
# list : ['abc',123,'xyz','789']
# list1 : ['abc',123,'xyz',456]
# list2 : ['abc',123,'xyz','789']
print('-'*25)

# Conclusion:
# pass by value is equal to list1 = list2[:]; list(); .copy() but not when we have list
# of lists


# __________________________________________________________________________________________________________________
# Mutable Default Argument
# https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
def f(x, lst=[]):
    for i in range(x):
        lst.append(i * i)
    print(lst)


f(2)              # [0, 1]
f(3, [3, 2, 1])   # [3, 2, 1, 0, 1, 4]
f(3)              # [0, 1, 0, 1, 4]      the list occupies the same memory location as the list from the first call
print('-'*25)

# __________________________________________________________________________________________________________________
# Pass by assignment (mixture of pass by reference & pass by value)
# https://www.youtube.com/watch?v=A9gtsfGgjvI
# https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
a = [1, 2, 3]
b = a
print(a, id(a), id(b), id(a) == id(b))
a = [3, 4, 5]
print(a, id(a), id(b), id(a) == id(b))

# Note: Regardless of list being mutable, when the list is assigned new values (pass by assignment), the the list is
# pointing to a new reference/id
