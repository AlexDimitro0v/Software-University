"""
A cookie factory accepts orders every day. Write a program to help the cookers to make the cookies faster by just
entering the necessary products/ingredients into the computer. Flour, sugar and eggs should always be present in the
mixture, but for the different types of biscuits - various additional product could be added and their number is
unlimited.

Input:
• The number of batches
• Then repeatedly on the next lines until the command "Bake!" is received, read:
    o The products in the mixture for the current batch
Output:
• If the mixture for the current batch does not contain at least 1 of the mandatory components, print:
    o "The batter should contain flour, eggs and sugar!"
• If the mixture for the current batch contain all of the mandatory components, print:
    o "Baking batch number {the current batch}..."
"""


def solve1(cooking):
    counter = 1
    mandatory_components = ['flour', 'sugar', 'eggs']
    while counter <= cooking:
        product = input()
        while product != 'Bake!':
            if product in mandatory_components:
                mandatory_components.remove(product)
            product = input()
        if not mandatory_components:
            # if all the ingredients are presence (the batter contain all of them and there aren't any left in the list)
            print(f"Baking batch number {counter}...")
            counter += 1
            mandatory_components = ['flour', 'sugar', 'eggs']       # resetting the ingredients
        else:
            # if some of them are missing
            print("The batter should contain flour, eggs and sugar!")


# Another Solution
def solve2(cooking):
    for batch in range(1, cooking+1):
        flour = False
        sugar = False
        eggs = False
        product = input()
        while True:
            if product == 'flour':
                flour = True
            elif product == 'sugar':
                sugar = True
            elif product == 'eggs':
                eggs = True
            elif product == 'Bake!':
                if flour and sugar and eggs:
                    print(f"Baking batch number {batch}...")
                    break
                else:
                    print("The batter should contain flour, eggs and sugar!")
            product = input()


def main():
    daily_cooking = int(input())
    solve1(daily_cooking)


if __name__ == '__main__':
    main()

