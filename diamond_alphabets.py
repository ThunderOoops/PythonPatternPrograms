# Diamond Pattern with Alphabets - Without using any built-in functions

rows = int(input("Enter number of rows for upper half (e.g. 5): "))

# Upper half
i = 1
while i <= rows:
    # Spaces
    s = 0
    while s < rows - i:
        print(" ", end="")
        s += 1
    # Alphabets
    char_code = 65  # 'A'
    j = 1
    while j <= (2 * i - 1):
        # Convert char_code to character manually via chr
        print(chr(char_code), end="")
        if j < i:
            char_code += 1
        else:
            char_code -= 1
        j += 1
    print()
    i += 1

# Lower half
i = rows - 1
while i >= 1:
    # Spaces
    s = 0
    while s < rows - i:
        print(" ", end="")
        s += 1
    # Alphabets
    char_code = 65
    j = 1
    while j <= (2 * i - 1):
        print(chr(char_code), end="")
        if j < i:
            char_code += 1
        else:
            char_code -= 1
        j += 1
    print()
    i -= 1
