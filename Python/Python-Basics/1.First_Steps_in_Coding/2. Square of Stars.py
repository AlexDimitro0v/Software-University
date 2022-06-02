# Create a Rectangle of stars
stars_number = int(input("Give a number of stars: "))


def square_of_stars(n):
    print(n * "*")
    for i in range(1, n - 1):               # (1,(n-2) +1)
        print("*" + " " * (n - 2) + "*")
    print(n * "*")


# Note: The python files can be used as reusable modules
# The Pythonic way to keep the printing part only within this file (useful when this file is being imported)
if __name__ == '__main__':
    # execute only if run as a script
    square_of_stars(stars_number)
