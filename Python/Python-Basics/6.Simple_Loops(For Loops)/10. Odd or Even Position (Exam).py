"""
Write a program that reads n number of integers (n>0) entered by the user and calculates the sum, the min and the max of
the numbers at odd, as well as at even positions (we start counting from 1). When there is no min/max number, print "No"

Input:
• First Line - n (the number of integers to be entered from the user).
• The next n lines - a single integer per line.
Output(6 Lines always):
1."OddSum=" + {sum of the numbers at odd positions},
2."OddMin=" + {minimum value among the numbers at odd positions} / {"No"},
3."OddMax=" + {maximum value among the numbers at odd numbers} / {"No"},
4."EvenSum=" + {sum of the numbers at even positions},
5."EvenMin=" + {minimum value among even-positioned numbers} / {"No"},
6."EvenMax=" + {maximum value among even-positioned numbers} / {"No"}

Note: Be careful for the commas between the lines.
"""


def solve(n):
    numbers_list = [None] * n                 # Creating an empty list
    answer = []                               # Will contain the answer list

    for number in range(n):
        num = float(input())
        numbers_list[number] = num            # Storing each number in the list

    # ------------------------------------------------------------------------------------------------------------
    # Now, we have to filter the even and odd-positioned numbers from the numbers_list, there are several ways to do it:

    # 1. List Slicing
    # https://coderwall.com/p/rujmya/get-odd-and-even-indexed-values-from-list-in-python
    # https://stackoverflow.com/questions/12433695/extract-elements-of-list-at-odd-positions
    odd_positioned_elements = numbers_list[::2]
    even_positioned_elements = numbers_list[1::2]

    # 2.List Comprehension and enumerate function
    # odd_positioned_elements = [v for k, v in enumerate(numbers_list) if k % 2 == 0]
    # even_positioned_elements = [v for k, v in enumerate(numbers_list) if k % 2]

    # Note: We have to consider that we start counting from 1, not from 0.
    # ------------------------------------------------------------------------------------------------------------

    # The odd part
    try:
        sum_odd = sum(odd_positioned_elements)
        answer.append(f"OddSum={sum_odd:.2f}")
    except ValueError:
        answer.append("OddSum=0")
    try:
        min_odd = min(odd_positioned_elements)
        max_odd = max(odd_positioned_elements)
        answer.extend([f"OddMin={min_odd:.2f}", f"OddMax={max_odd:.2f}"])
    except ValueError:
        answer.extend(["OddMin=No", "OddMax=No"])
    # The even part
    try:
        sum_even = sum(even_positioned_elements)
        answer.append(f"EvenSum={sum_even:.2f}")
    except ValueError:
        answer.append("EvenSum=0")
    try:
        min_even = min(even_positioned_elements)
        max_even = max(even_positioned_elements)
        answer.extend([f"EvenMin={min_even:.2f}", f"EvenMax={max_even:.2f}"])
    except ValueError:
        answer.extend(["EvenMin=No", "EvenMax=No"])

    return answer


def solve2(n):
    sum_even = 0
    sum_odd = 0

    max_even = float('-inf')
    max_odd = float('-inf')

    min_even = float('inf')
    min_odd = float('inf')

    for disc_number in range(1, n+1):
        number = float(input())

        # even
        if disc_number % 2 == 0:
            sum_even += number
            if number > max_even:
                max_even = number

            if number < min_even:
                min_even = number

        # odd
        else:
            sum_odd += number
            if number < min_odd:
                min_odd = number
            if number > max_odd:
                max_odd = number
    # odd
    print("OddSum=%.2f," % sum_odd)
    if not min_odd == float('inf'):
        print("OddMin=%.2f," % min_odd)
    else:
        print("OddMin=No,")
    if not max_odd == float('-inf'):
        print("OddMax=%.2f," % max_odd)
    else:
        print("OddMax=No,")

    # even
    print("EvenSum=%.2f," % sum_even)
    if not min_even == float('inf'):
        print("EvenMin=%.2f," % min_even)
    else:
        print("EvenMin=No,")
    if not max_even == float('-inf'):
        print("EvenMax=%.2f" % max_even)
    else:
        print("EvenMax=No")


def main():
    n = int(input())
    print(',\n'.join(solve(n)))


if __name__ == '__main__':
    main()

