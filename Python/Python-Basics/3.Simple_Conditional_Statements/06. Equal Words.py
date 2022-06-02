"""
Write a program that compares two inputted words and checks if the contain the same characters.
Note: You should not distinguish between capital and non-capital letters. Output yes or no in response of the comparison.
"""


def compare_words(word1, word2):
    if word1 == word2:
        return True
    return False


if __name__ == '__main__':
    w1 = input("Enter the first word: ").lower()     # .upper()
    w2 = input("Enter the second word: ").lower()    # .upper() works as well
    if compare_words(w1, w2) is True:
        print("yes")
    else:
        print("no")
