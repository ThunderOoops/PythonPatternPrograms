# Pyramid Pattern Program - Without using any built-in functions

rows = int(input("Enter number of rows: "))

i = 1
while i <= rows:
    # Print leading spaces
    spaces = rows - i
    s = 0
    while s < spaces:
        print(" ", end="")
        s += 1
    # Print stars
    stars = 0
    while stars < (2 * i - 1):
        print("*", end="")
        stars += 1
    print()
    i += 1
