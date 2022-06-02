"""
Write a program that given a string entered by the user, calculates the sum of the vowel letters according to the values
below:
a = 1
e = 2
i = 3
o = 4
u = 5
"""


def count_vowel_values(word):
    """
    # get key from a dictionary
    vowels = {"a":1, "e":2, "i":3, "o":4, "u":5}
    for key in vowels:
        print(vowels[key]) (1,2,3,4,5)   or    print(key)  (a,e,i,o,u)
    """
    vowels = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
    count = 0

    for letter in word:
        if letter in vowels:
            count += vowels[letter]

    return count


# wanted-way
def count_vowel_values2(word):
    total_sum = 0

    for i in range(0, len(word)):
        if word[i] == 'a':
            total_sum += 1

        if word[i] == 'e':
            total_sum += 2

        if word[i] == 'i':
            total_sum += 3

        if word[i] == 'o':
            total_sum += 4

        if word[i] == 'u':
            total_sum += 5

    return total_sum


# another way
def count_vowel_values3(word):
    vowels = {"a": 1,
              "e": 2,
              "i": 3,
              "o": 4,
              "u": 5
              }

    total_sum = 0
    for letter_index in range(0, len(word)):
        current_letter = word[letter_index]

        if current_letter in vowels:
            total_sum += vowels[current_letter]

    return total_sum


if __name__ == '__main__':
    string = input().lower()
    print(count_vowel_values(string))
