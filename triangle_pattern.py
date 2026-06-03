# Triangle Pattern Program - Without using any built-in functions

rows = int(input("Enter number of rows: "))

i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
