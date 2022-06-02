"""
Annie goes back to her hometown after a very long period abroad. Getting home, she sees her grandmother's old library
and remembers her favorite book. Write a program to help Annie find her favorite book. Until Annie does not find her
favorite book or check every book title in the library, she will keep searching.

Input:
• The title of Annie's favorite book (string)
• N - The capacity of the library, i.e the number of books (int)
• The next N lines - a title of a book. 
Output:
• If Annie finds the book - break the program and print:
    o "You checked {number} books and found it."
• If Annie doesn't find the book, print:
    o "The book you search is not here!"
    o "You checked {number} books."
"""


def solve(book, library_size):
    counter = 0
    for i in range(library_size):
        name = input()
        if book == name:
            return f"You checked {i} books and found it."
        counter += 1
    print("The book you search is not here!")
    return f"You checked {counter} books."


def solve2(book, library_size):
    counter = 0
    is_found = False
    while counter < library_size:
        name = input()
        if name == book:
            is_found = True
            break
        counter += 1        #
    if is_found:
        return f"You checked {counter} books and found it."
    else:
        print("The book you search is not here!")
        return f"You checked {counter} books."


def main():
    name = input()
    library_size = int(input())
    print(solve2(name, library_size))


if __name__ == '__main__':
    main()
