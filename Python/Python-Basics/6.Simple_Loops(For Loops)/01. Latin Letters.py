def print_all_latin_letters():
    for letter in range(ord("a"), ord("z")+1):
        print(chr(letter), end=" ")


print_all_latin_letters()

# The ord() method returns an integer representing Unicode code point for the given Unicode character.
# The chr() method returns a character (a string) from an integer (represents unicode code point of the character)
# See the ASCII Table
