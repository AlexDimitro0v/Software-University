from itertools import product, permutations
"""
1. cartesian product, equivalent to a nested for-loop:
   product('ABCD', repeat=2)                  AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

2. R-length tuples, all possible orderings, no repeated elements:
   permutations('ABCD', 2)                    AB AC AD BA BC BD CA CB CD DA DB DC
   
3. R-length tuples, in sorted order, no repeated elements:
   combinations('ABCD', 2)                    AB AC AD BC BD CD

4. R-length tuples, in sorted order, with repeated elements:
   combinations_with_replacement('ABCD', 2)   AA AB AC AD BB BC BD CC CD DD
"""


# A solution can find all permutations of a word and if a match to the other words is
# found, we have a solution

def anagrams_2(word1, word2):
    # Chaining
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')
    
    for permutation in permutations(word1):
        w = ''.join(permutation)
        
        if w == word2:
            return True
    return False


def anagrams(word1: str, word2: str):
    """
    Algorithm:
    1. Cast arguments to lowercase strings
    2. Remove any whitespaces
    3. Check if the letters of a word are the same with the letters of another word
    independent of the order
    """
    try:
        # Chaining
        word1 = str(word1.lower().replace(' ', ''))
        word2 = str(word2.lower().replace(' ', ''))
        histogram1 = char_histogram(word1)
        histogram2 = char_histogram(word2)
        print(f"{histogram1}\n{histogram2}")
        # return histogram1 == histogram2
        return set(word1) == set(word2) and len(word1) == len(word2)
        # return sorted(word1) == sorted(word2)
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


def char_histogram(string):
    dd = {}
    for char in string:
        dd[char] = dd.get(char, 0) + 1
    return dict(sorted(dd.items(), key=lambda item: item[0]))


if __name__ == '__main__':
    tests = [
        ("listen", "silent", True),
        ("LISTEN", "silent", True),
        ("python", "ruby", False),
        ("New York Times", "monkeys writing", False),
        ("snake", "sssnakee", False),
    ]
    
    for word1, word2, expected in tests:
        result = anagrams(word1, word2)
        print(result == expected)
