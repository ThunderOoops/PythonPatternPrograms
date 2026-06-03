# Convert a List into Cubes - Only for Odd Numbers

# Input list from user
n = int(input("Enter number of elements in the list: "))

numbers = []
i = 0
while i < n:
    val = int(input("Enter element " + str(i + 1) + ": "))
    numbers.append(val)
    i += 1

print("\nOriginal List:", numbers)

result = []
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        result.append(numbers[i] ** 3)
    i += 1

print("Cubes of Odd Numbers:", result)
