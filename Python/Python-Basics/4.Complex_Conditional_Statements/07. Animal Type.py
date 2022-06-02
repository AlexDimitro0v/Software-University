"""
Write a program that prints the animal's class according to its name inputted from the user.
"""

mammal = ["dog"]
reptile = ["crocodile", "tortoise", "snake"]
# another way with a dictionary
animal_dictionary = {
    "mammal": ["dog"],
    "reptile": ["crocodile", "tortoise", "snake"]
}


def class_animal(animal):
    if animal in mammal:
        print("mammal")
    elif animal in reptile:
        print("reptile")
    else:
        print("unknown")


def class_animal2(animal):          # bad-performance solution
    animal_unknown = "unknown"
    for key in animal_dictionary.keys():
        values = animal_dictionary[key]
        if animal in values:
            animal_unknown = key

    print(animal_unknown)


def main():
    animal = input("Give me an animal: ")
    class_animal(animal)


if __name__ == '__main__':
    main()
